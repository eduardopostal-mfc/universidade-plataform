#!/usr/bin/env python3
"""Monta os blocos de legenda (tempos no vídeo final) a partir das palavras com tempo
(palavras.py) e da lista de cortes. Uso:
  python legenda-blocos.py palavras.json "26.1-42.8,56.5-67.5" [max_palavras=4]
Imprime um JSON com [{inicio, fim, texto}] para colar em gravado.json → "legenda"."""
import sys, json, re
words = json.load(open(sys.argv[1]))
cortes = [tuple(float(x) for x in c.split("-")) for c in sys.argv[2].split(",")]
maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 4
blocos, off = [], 0.0
for a, b in cortes:
    ws = [w for w in words if w["t0"] >= a - 0.05 and w["t1"] <= b + 0.05]
    buf = []
    def fecha():
        if buf:
            blocos.append({"inicio": round(buf[0]["t0"] - a + off, 2), "fim": round(buf[-1]["t1"] - a + off + 0.15, 2),
                           "texto": " ".join(x["w"] for x in buf)})
            buf.clear()
    for w in ws:
        buf.append(w)
        if len(buf) >= maxp or re.search(r"[.!?,;:]$", w["w"]):
            fecha()
    fecha()
    off += b - a
for i in range(1, len(blocos)):
    if blocos[i]["inicio"] < blocos[i - 1]["fim"]:
        blocos[i - 1]["fim"] = blocos[i]["inicio"]
print(json.dumps(blocos, ensure_ascii=False, indent=1))
