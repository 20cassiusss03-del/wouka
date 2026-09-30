# -*- coding: utf-8 -*-
"""Тайминг кадров по озвучке: timing_nuclear.json + shots_nuclear.py → frames_nuclear.json / .csv.

Кадр начинается с начала своей первой строки и длится до начала следующего кадра.
Кадры на одной и той же группе строк делят её время поровну.
"""
import csv
import json
import pathlib

from shots_nuclear import SHOTS

HERE = pathlib.Path(__file__).parent
T = {r["n"]: r for r in json.loads((HERE / "timing_nuclear.json").read_text(encoding="utf-8"))}
END = max(r["end"] for r in T.values()) + 0.8

starts = []
i = 0
while i < len(SHOTS):
    a, b = SHOTS[i]["a"], SHOTS[i]["b"]
    j = i
    while j + 1 < len(SHOTS) and (SHOTS[j + 1]["a"], SHOTS[j + 1]["b"]) == (a, b):
        j += 1
    s0, s1 = T[a]["start"], T[b]["end"]
    k = j - i + 1
    for m in range(k):
        starts.append(s0 + (s1 - s0) * m / k)
    i = j + 1
starts[0] = 0.0

rows = []
for i, s in enumerate(SHOTS):
    end = starts[i + 1] if i + 1 < len(SHOTS) else END
    rows.append(dict(id="n%03d" % (i + 1), start=round(starts[i], 2), dur=round(end - starts[i], 2),
                     kind=s["mode"] or "scene", img="" if s["mode"] == "chart" else "n%03d.jpg" % (i + 1),
                     chart=s["what"] if s["mode"] == "chart" else "", lines="%d-%d" % (s["a"], s["b"])))
(HERE / "frames_nuclear.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
with open(HERE / "frames_nuclear.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
d = [r["dur"] for r in rows]
print("кадров %d, длина %.1f с, кадр: мин %.1f / средн %.1f / макс %.1f с" % (len(rows), END, min(d), sum(d) / len(d), max(d)))
for r in rows:
    if r["dur"] > 9 or r["dur"] < 1.5:
        print("  проверить:", r["id"], r["dur"], "с, строки", r["lines"])
