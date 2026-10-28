import sys, json
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = m.transcribe(src, language="pt", vad_filter=True, word_timestamps=True, beam_size=2)
words = []
for s in segs:
    for w in s.words or []:
        words.append({"t0": round(w.start, 2), "t1": round(w.end, 2), "w": w.word.strip()})
json.dump(words, open(out, "w"), ensure_ascii=False)
print("palavras:", len(words))
