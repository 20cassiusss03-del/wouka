# -*- coding: utf-8 -*-
"""Выравнивание озвучки по строкам сценария без распознавания речи.

Ищем паузы в аудио и выбираем среди них 95 границ между 96 строками так,
чтобы длительность каждой строки была пропорциональна числу букв в ней,
а границы по возможности приходились на длинные паузы.

    python align_nuclear.py voice.mp3   → timing_nuclear.json, _check_nuclear.txt
"""
import json
import math
import pathlib
import subprocess
import sys

import imageio_ffmpeg
import numpy as np

HERE = pathlib.Path(__file__).parent
SR = 16000
HOP = 160            # 10 мс
MIN_PAUSE = 0.18     # с


def load(path):
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    raw = subprocess.run([ff, "-v", "quiet", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768


def pauses(x):
    n = len(x) // HOP
    rms = np.sqrt((x[:n * HOP].reshape(n, HOP) ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(rms)
    thr = np.percentile(db, 10) + 12          # порог тишины от уровня шума
    quiet = db < thr
    out, i = [], 0
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]:
                j += 1
            if (j - i) * HOP / SR >= MIN_PAUSE:
                out.append((i * HOP / SR, j * HOP / SR))
            i = j
        else:
            i += 1
    total = n * HOP / SR
    return out, total


def main():
    audio = sys.argv[1]
    lines = [l.strip() for l in (HERE / "script_nuclear.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    x = load(audio)
    ps, total = pauses(x)
    # речь начинается после первой паузы в начале и кончается перед последней
    t0 = ps[0][1] if ps and ps[0][0] < 0.05 else 0.0
    t1 = ps[-1][0] if ps and ps[-1][1] > total - 0.05 else total
    inner = [p for p in ps if p[0] > t0 + 0.5 and p[1] < t1 - 0.5]
    # узлы: начало, паузы, конец
    starts = [t0] + [p[1] for p in inner]          # где может начаться строка
    ends = [p[0] for p in inner] + [t1]            # где может кончиться строка
    plen = [p[1] - p[0] for p in inner]
    L, P = len(lines), len(inner)
    chars = np.array([len(l) for l in lines], float)
    rate = (t1 - t0) / chars.sum()
    INF = 1e18
    # dp[i][k]: строки 0..i-1 размещены, строка i начинается после паузы k (k=-1 → t0)
    dp = np.full((L + 1, P + 2), INF)
    back = np.zeros((L + 1, P + 2), int)
    dp[0][0] = 0.0   # индекс 0 = старт t0, индекс k+1 = после паузы k
    for i in range(L):
        exp = chars[i] * rate
        for k in range(P + 1):
            if dp[i][k] >= INF:
                continue
            s = starts[k]
            last = (i == L - 1)
            cands = [P] if last else range(k, P)
            for m in cands:
                e = ends[m]
                d = e - s
                if d <= 0.3:
                    continue
                if d > exp * 3.5 and not last:
                    break
                c = math.log(d / exp) ** 2
                if not last:
                    c -= 0.8 * min(plen[m], 1.2)      # бонус за длинную паузу
                nk = m + 1
                if dp[i][k] + c < dp[i + 1][nk]:
                    dp[i + 1][nk] = dp[i][k] + c
                    back[i + 1][nk] = k
    k = P + 1                                   # последняя строка кончается в t1
    seq = []
    for i in range(L, 0, -1):
        pk = back[i][k]
        seq.append((pk, k))
        k = pk
    seq.reverse()
    res = []
    for i, (a, b) in enumerate(seq):
        s = starts[a]
        e = ends[b - 1]
        res.append(dict(n=i + 1, start=round(s, 2), end=round(e, 2), text=lines[i]))
    (HERE / "timing_nuclear.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(HERE / "_check_nuclear.txt", "w", encoding="utf-8") as f:
        for r in res:
            d = r["end"] - r["start"]
            f.write("%3d %6.2f %6.2f %5.2fс %5.2f %s\n" % (r["n"], r["start"], r["end"], d,
                                                       d / (len(r["text"]) * rate), r["text"][:60]))
    print("пауз найдено:", P, "| речь %.1f–%.1f с | строк %d" % (t0, t1, L))


if __name__ == "__main__":
    main()
