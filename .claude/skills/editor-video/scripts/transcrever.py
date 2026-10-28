import sys, os, glob
from faster_whisper import WhisperModel
out = sys.argv[1]; files = sys.argv[2:]
model = WhisperModel("small", device="cpu", compute_type="int8")
for f in files:
    base = os.path.splitext(os.path.basename(f))[0]
    dst = os.path.join(out, base + ".txt")
    if os.path.exists(dst): continue
    segs, info = model.transcribe(f, language="pt", vad_filter=True, beam_size=1)
    with open(dst + ".tmp", "w", encoding="utf-8") as w:
        for s in segs:
            w.write(f"[{s.start:7.1f}–{s.end:7.1f}] {s.text.strip()}\n")
    os.rename(dst + ".tmp", dst); print("ok", base, flush=True)
