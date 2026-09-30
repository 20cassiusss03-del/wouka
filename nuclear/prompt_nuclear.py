# -*- coding: utf-8 -*-
"""Собирает промпты Flow из shots_nuclear.py (Danger Premium) по общему стилю каналов (см. ../FLOW_STYLE.md).

    python prompt_nuclear.py          # проверка + запись ПРОМПТЫ_ядерщики.txt и prompts_nuclear.json
    python prompt_nuclear.py n042     # показать один промпт
"""
import json
import pathlib
import re
import sys

from shots_nuclear import SHOTS

HERE = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- стиль (из прошлой сессии)
STYLE = ("Flat 2D cartoon illustration, thick black outlines, flat colours, no shading, "
         "no gradients, 16:9. A friendly palette of flat, real colours: soft teal, warm wood, "
         "cream, muted green, clay and grey-blue, never washed out and never grey all over. "
         "The one subject of the shot carries the strongest and warmest colour in the frame. ")
ROOM_LOOK = ("The place is calm, tidy and minimal: walls, floor, two or three large pieces of "
             "furniture and one green plant or similar spot of life. The wall, the floor and the "
             "furniture are NOT all the same colour: the place uses at least three different flat "
             "colours. No crowd of small props, no busy detail. ")
SUBJECT = "One single subject fills about half the frame, with the strongest colour and the highest contrast. "
PEOPLE = "Only the characters named below are in the shot; nobody else unless the shot says so. "
NOTEXT = ("NO TEXT, no letters, no numbers, no labels anywhere in the image. No brand logos. "
          "A plain radiation trefoil symbol without letters is allowed. ")
BAKE_LINE = ("Written large across the main object of this shot, %s, is this and nothing else: %s. "
             "Spell it exactly like that. The lettering is big enough to read at a glance, taking up a "
             "large part of the frame, even if the object it is on has to be drawn bigger or closer. "
             "There is no other writing anywhere in the picture. No brand logos. ")
TEXT_WORD = "in clean bold black capitals"
TEXT_NUM = ["in huge bold red numerals with a thick white outline",
            "in huge bold white numerals on a bright red panel",
            "in huge bold white numerals on a teal panel"]

# ---------------------------------------------------------------- персонажи
COON = ("The raccoon is the channel mascot: a cartoon raccoon standing upright like a person, "
        "black bandit mask across the eyes, large white expressive eyes, a brave, slightly nervous face. "
        "Exactly the same raccoon design every time. Only ONE raccoon in the picture. ")
COON_JACKET = "Unless the shot says otherwise, he wears a bright orange high-visibility work jacket with silver reflective stripes. "
COON_SUIT = ("In this shot the raccoon wears a bright yellow plastic full-body protective bubble suit that "
             "covers him from feet to head, a clear round plastic hood over his face, yellow gloves, and a "
             "thick grey air hose running from his back. ")
TIMER = ("The timekeeper is a recurring character: a simple cartoon person, plain round head, short grey "
         "hair, large round white eyes with small black pupils, white cotton coveralls, a big silver "
         "stopwatch in his hand. Exactly the same design every time. ")
MANAGER = ("The plant manager is a recurring character: a simple cartoon man, plain round head, "
           "thinning brown hair, large round white eyes with small black pupils, a short-sleeved white "
           "shirt and a dark tie. Exactly the same design every time. ")
PEOPLE_LOOK = ("Every human is drawn as a simple cartoon person with a plain round head and large round "
               "white eyes with small black pupils, in the same flat style. ")


def cast(what):
    w = what.lower()
    out = []
    if "raccoon" in w:
        out.append(COON)
        out.append(COON_SUIT if "yellow suit" in w else COON_JACKET)
    if "timekeeper" in w:
        out.append(TIMER)
    if "plant manager" in w:
        out.append(MANAGER)
    out.append(PEOPLE_LOOK)
    return "".join(out)


# ---------------------------------------------------------------- места
ROOMS = {
    "platform": "Place: deep inside a nuclear plant: a steel grating platform under the rounded bottom of a giant pale-green steel tank, grey concrete walls, a yellow-and-magenta rope barrier, bright work lamps. ",
    "bowl": "Place: inside the bottom chamber of a steam generator: a curved dome of dull steel, a flat ceiling full of small tube holes, two big round pipe openings, a faint green glow. ",
    "cutaway": "Place: a clean simple cutaway illustration on a plain cream background, like a friendly textbook picture. ",
    "plant": "Place: outside a nuclear power plant: two big cooling towers, a concrete dome, a fence, green grass, a wide sky. ",
    "plant_tmi": "Place: an island in a wide river with a nuclear plant, two tall cooling towers, trees on the banks. ",
    "plant_mi": "Place: a sandy lake shore with dunes and a nuclear plant with one concrete dome. ",
    "turbine": "Place: a huge turbine hall: a long green turbine, yellow railings, tall windows, a crane rail above. ",
    "control": "Place: a 1970s control room: long mint-green panels full of dials and switches, beige desks, operators. ",
    "pool": "Place: a refueling floor: a deep glowing blue pool, a yellow bridge crane over it, grey concrete. ",
    "locker": "Place: a changing room at a nuclear plant: grey-blue lockers, wooden benches, yellow suits hanging on hooks. ",
    "locker_old": "Place: a 1970s changing room: olive-green lockers, a wooden bench, white paper coveralls on hooks, a round wall clock. ",
    "office": "Place: a plant manager's office: wood panelling, a big steel desk with papers, grey filing cabinets, a window showing a cooling tower. ",
    "clinic": "Place: a doctor's office: pale teal walls, an X-ray lightbox, an examination bench. ",
    "gate_old": "Place: a nuclear plant gate in the 1970s: a chain-link fence, a guard booth, old cars in the lot, a cooling tower behind. ",
    "floor_old": "Place: a concrete work floor inside a plant in the 1970s: grey walls painted half yellow, pipes overhead, a yellow-and-magenta rope barrier. ",
    "newsroom": "Place: a small cluttered 1980s office: mustard wall, a typewriter, stacks of paper reports, a desk lamp. ",
    "road_old": "Place: an American highway at night in the 1970s: dark fields, a two-lane road, a warm glow on the horizon. ",
    "motel": "Place: a cheap roadside motel room: orange bedspread, wood panelling, a small TV, a window with a neon glow. ",
    "beach": "Place: a sunny beach: turquoise water, yellow sand, a striped umbrella. ",
    "mockup": "Place: a training hall: a full-size model of the rounded bottom of a steam generator made of plywood and steel, a ladder and platform under it, bright lights. ",
    "japan_map": "Place: a plain paper map on a wooden table, soft light. ",
    "japan_desk": "Place: a small Japanese study room: tatami floor, a low wooden desk, shoji paper screens, a stack of books. ",
    "yoseba": "Place: a street corner in a Japanese city at dawn: low concrete buildings, power lines, vending machines glowing, a grey sky. ",
    "fukushima": "Place: a damaged coastal nuclear plant in Japan: broken grey reactor buildings, rubble, the dark sea behind, cranes. ",
    "japan_room": "Place: a small plain Japanese apartment: a low table, a rice cooker, beige walls, a window with rain. ",
    "sendai": "Place: a big Japanese train station concourse before dawn: tiled floor, closed shop shutters, cold blue light. ",
    "chernobyl": "Place: the smashed roof of a Soviet reactor building in 1986: black chunks of debris, twisted steel, a grey sky. ",
    "study": "Place: a university research office: shelves of journals, a big desk with a computer, a green plant. ",
    "home": "Place: a cosy living room: dusty-pink wall, a mustard sofa, a sunny window, a green plant. ",
    "datacenter": "Place: a huge modern data center hall: long rows of black server racks with blue lights, a polished floor. ",
    "gate": "Place: a modern nuclear plant gate at dawn: a security fence, a parking lot, cooling towers behind. ",
    "laptop": "Place: a close view of a laptop on a cheap motel table next to a coffee cup. ",
}
TINTS = ["The light is warm and golden. ", "The light is cool and bluish. ",
         "The light is warm and orange. ", "The light is cool and teal. "]
CLOSE_WORDS = ("seen close", "close view", "close-up")
WIDE_WORDS = ("wide view", "seen wide", "from above")


def sid(i):
    return "n%03d" % (i + 1)


def scale(s):
    w = s["what"].lower()
    if any(k in w for k in CLOSE_WORDS):
        return "Close-up shot. "
    if any(k in w for k in WIDE_WORDS):
        return "Wide establishing shot. "
    return "Medium shot. "


def text_style(i, txt):
    if re.search(r"\d", txt):
        return TEXT_NUM[i % len(TEXT_NUM)]
    return TEXT_WORD




def prompt(i):
    s = SHOTS[i]
    parts = [STYLE, ROOM_LOOK, SUBJECT, PEOPLE]
    parts.append(BAKE_LINE % (text_style(i, s["txt"]), s["txt"]) if s["txt"] else NOTEXT)
    parts.append(ROOMS[s["room"]])
    parts.append(TINTS[i % len(TINTS)])
    parts.append(scale(s))
    parts.append(cast(s["what"]))
    parts.append(s["what"])
    return "".join(parts).strip()


def check():
    errs = []
    covered = set()
    for i, s in enumerate(SHOTS):
        covered.update(range(s["a"], s["b"] + 1))
        if s["mode"] == "chart":
            continue
        if s["room"] not in ROOMS:
            errs.append("%s: нет комнаты %s" % (sid(i), s["room"]))
        if s["txt"] and len(re.sub(r"[^\w\s]", "", s["txt"]).split()) > 4:
            errs.append("%s: надпись длиннее 4 слов" % sid(i))
        if "two raccoon" in s["what"].lower():
            errs.append("%s: два енота" % sid(i))
    n = sum(1 for l in open(HERE / "script_nuclear.txt", encoding="utf-8") if l.strip())
    miss = sorted(set(range(1, n + 1)) - covered)
    if miss:
        errs.append("строки без кадра: %s" % miss)
    return errs


def main():
    if len(sys.argv) > 1:
        i = int(sys.argv[1].lstrip("dn")) - 1
        print(prompt(i))
        return
    errs = check()
    for e in errs:
        print("ОШИБКА:", e)
    if errs:
        sys.exit(1)

    out, data, batch = [], [], 0
    flow = [i for i, s in enumerate(SHOTS) if s["mode"] != "chart"]
    out.append("ПРОМПТЫ ДЛЯ FLOW — «Nuclear Plants Hired Him for 12 Minutes»")
    out.append("Nano Banana 2 · 16:9 · x1. Один промпт = одна картинка. Пачки по 10, после пачки скачать в 2K.")
    out.append("Имя файла при сохранении = номер кадра (n001.jpg …).")
    out.append("")
    for k, i in enumerate(flow):
        if k % 10 == 0:
            batch += 1
            out.append("=" * 20 + " ПАЧКА %d " % batch + "=" * 20)
            out.append("")
        s = SHOTS[i]
        out.append("[%s] строки %d–%d%s" % (sid(i), s["a"], s["b"], (" · надпись: " + s["txt"]) if s["txt"] else ""))
        out.append(prompt(i))
        out.append("")
    out.append("=" * 20 + " СХЕМЫ ДЛЯ МОНТАЖА (во Flow не генерировать) " + "=" * 20)
    for i, s in enumerate(SHOTS):
        if s["mode"] == "chart":
            out.append("[%s] строки %d–%d: %s" % (sid(i), s["a"], s["b"], s["what"]))
    for i, s in enumerate(SHOTS):
        data.append(dict(id=sid(i), a=s["a"], b=s["b"], mode=s["mode"] or "scene", txt=s["txt"],
                         prompt=prompt(i) if s["mode"] != "chart" else "", chart=s["what"] if s["mode"] == "chart" else ""))
    (HERE / "ПРОМПТЫ_ядерщики.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    (HERE / "prompts_nuclear.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("готово: %d кадров, %d для Flow, %d схем, %d пачек" % (len(SHOTS), len(flow), len(SHOTS) - len(flow), batch))


if __name__ == "__main__":
    main()
