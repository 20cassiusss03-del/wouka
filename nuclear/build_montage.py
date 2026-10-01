# -*- coding: utf-8 -*-
"""Собирает props для OpenMontage (remotion-composer, композиция Explainer).

    python build_montage.py  →  montage_nuclear.json
Кадры: public/nuclear/nNNN.jpg, озвучка: public/nuclear/voice.mp3.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent
F = json.loads((HERE / "frames_nuclear.json").read_text(encoding="utf-8"))
T = {r["n"]: r for r in json.loads((HERE / "timing_nuclear.json").read_text(encoding="utf-8"))}

ACC = "#D35400"
CHARTS = {
    "n040": dict(type="stat_card", stat="3 rem", subtitle="per quarter · the rule before 1994"),
    "n041": dict(type="stat_card", stat="5 rem", subtitle="per year · the limit since 1994"),
    "n042": dict(type="comparison", title="One year of radiation",
                 leftLabel="Legal limit for a nuclear worker", leftValue="50 mSv",
                 rightLabel="Average American, all sources", rightValue="≈6 mSv"),
    "n044": dict(type="comparison", title="One year at the legal limit equals",
                 leftLabel="years of ordinary life", leftValue="≈8",
                 rightLabel="chest X-rays", rightValue="≈2,500"),
    "n057": dict(type="comparison", title="US workers exposed to radiation",
                 leftLabel="1978", leftValue="44,000", rightLabel="1980", rightValue="77,000"),
    "n105": dict(type="stat_card", stat="309,932", subtitle="nuclear workers in France, the UK and the US · INWORKS, 2023"),
    "n106": dict(type="stat_card", stat="+2–3%", subtitle="relative risk of cancer death · one full year at the US limit"),
    "n123": dict(type="stat_card", stat="0.16 rem", subtitle="average measurable dose, US reactor workers, 2023"),
}
ANIMS = ["zoom-in", "zoom-out", "ken-burns", "pan-left", "pan-right"]

cuts = []
for i, r in enumerate(F):
    c = dict(id=r["id"], in_seconds=r["start"], out_seconds=round(r["start"] + r["dur"], 2))
    if r["kind"] == "chart":
        c.update(CHARTS[r["id"]], source="", accentColor=ACC, backgroundColor="#F4EBD9")
    else:
        c.update(source="nuclear/" + r["img"], animation=ANIMS[i % 2])
    cuts.append(c)

# Счётчик дозы: появляется на строке 12 («Keep an eye on the corner…»),
# считает 25 rem/ч (худший случай из сценария) с начала строки 13 до конца ролика.
start = T[13]["start"]
end = cuts[-1]["out_seconds"]
overlays = [
    dict(type="dose_counter", in_seconds=T[12]["start"], out_seconds=start, remPerHour=0.0),
    dict(type="dose_counter", in_seconds=start, out_seconds=end, remPerHour=25, yearRem=0.62, limitRem=5),
]
props = dict(theme="clean-professional", cuts=cuts, overlays=overlays,
             audio=dict(narration=dict(src="nuclear/voice.mp3", volume=1.0)))
(HERE / "montage_nuclear.json").write_text(json.dumps(props, ensure_ascii=False, indent=1), encoding="utf-8")
print("cuts", len(cuts), "end %.1f s" % end)
