# -*- coding: utf-8 -*-
"""Собирает промпты Flow из shots_delivery.py по стилю Dirty Margins (см. ../FLOW_STYLE.md).

    python prompt_delivery.py          # проверка + запись ПРОМПТЫ_доставка.txt и prompts_delivery.json
    python prompt_delivery.py d042     # показать один промпт
"""
import json
import pathlib
import re
import sys

from shots_delivery import SHOTS

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
NOTEXT = "NO TEXT, no letters, no numbers, no signs, no labels anywhere in the image. No brand logos. "
BAKE_LINE = ("Written large directly on the object named in the shot description, %s, is this and nothing else: %s. "
             "Spell it exactly like that. The lettering is part of that object itself: do NOT add a separate sign, "
             "board, banner, panel or label for it. It is big enough to read at a glance, even if the object has to "
             "be drawn bigger or closer. There is no other writing, no other numbers and no small print anywhere in "
             "the picture. No brand logos. ")
TEXT_WORD = "in clean bold black capitals"
TEXT_NUM = ["in huge bold red numerals with a thick white outline",
            "in huge bold black numerals",
            "in huge bold white numerals with a thick black outline"]

# ---------------------------------------------------------------- персонажи
COON = ("The raccoon is the channel mascot: a cartoon raccoon standing upright like a person, "
        "black bandit mask across the eyes, large white eyes, a sly narrow-eyed grin, wearing a "
        "dark green shop apron over a white shirt with rolled sleeves. Exactly the same raccoon "
        "design every time. Only ONE raccoon in the picture. ")
COON_EYES = ("His eyes are NOT the round friendly eyes used elsewhere in this style: they are narrowed "
             "to sly slits, half-closed, with the mouth curled up on one side in a crafty, scheming smile. ")
CUST = ("The customer in the grey coat is the channel's second recurring character: a simple cartoon "
        "person, plain round head, short reddish-brown hair, large round white eyes with small black "
        "pupils, wearing a grey coat over a cream sweater. Exactly the same design every time. ")
DRIVER = ("The driver in the red hoodie is a recurring character: a simple cartoon person, plain round "
          "head, short curly black hair, large round white eyes with small black pupils, wearing a "
          "plain red hoodie and jeans. Exactly the same design every time. ")
COOK = ("The burger cook is a recurring character: a simple cartoon person, plain round head, a thick "
        "black moustache, large round white eyes with small black pupils, a white paper cook's hat and "
        "a white apron over a mustard T-shirt. Exactly the same design every time. ")
PIZZA = ("The pizza owner is a recurring character: a simple cartoon person, plain round bald head, a "
         "short grey beard, large round white eyes with small black pupils, a red apron over a white "
         "shirt. Exactly the same design every time. ")
WRITER = ("The writer with glasses is a simple cartoon person, plain round head, short dark hair, round "
          "black glasses, large round white eyes with small black pupils, a navy sweater. ")
CAST = [("raccoon", COON + COON_EYES), ("grey coat", CUST), ("grey-coat", CUST), ("red hoodie", DRIVER),
        ("burger cook", COOK), ("pizza owner", PIZZA), ("writer with glasses", WRITER)]

# ---------------------------------------------------------------- места (цвет прописан в каждом)
ROOMS = {
    "home": "Place: a small cosy living room at night: dusty-pink wall, mustard sofa, a dark window streaked with rain, a warm floor lamp, a green plant. ",
    "phone": "Place: a big smartphone seen up close, held over a mustard sofa cushion, the screen bright with flat colourful app shapes; behind it a softly drawn dusty-pink room. ",
    "doorstep": "Place: an apartment front door at night: teal door, a brown doormat, a warm porch lamp, rain falling behind. ",
    "burger": "Place: a small friendly burger restaurant: teal wall, red-and-cream checkered floor, a warm wood counter with a register, a chalkboard menu on the wall, a green plant. ",
    "kitchen": "Place: the back kitchen of a burger restaurant: turquoise wall tiles, a steel grill and fryer, a warm wood prep table, a ticket printer, a green herb pot. ",
    "street": "Place: a city street at night in the rain: brick buildings in clay red, teal and cream, glowing streetlights, wet asphalt with coloured reflections. ",
    "car": "Place: inside a parked small car at night: the dashboard, the steering wheel, a phone in a holder, rain on the windscreen, streetlights outside. ",
    "parking": "Place: a big parking lot at night in the rain: yellow lines, tall lamps, a glowing fast-food sign shape far away with no letters. ",
    "gas": "Place: a gas station at night: a teal canopy, a bright red pump, clean white light, wet ground. ",
    "office": "Place: a sleek app company office: grey-blue wall, warm wood desk, a big window over the night city, a corkboard, a green plant. ",
    "support": "Place: a call centre desk: olive-green wall, a headset, a computer, a wall clock, a green plant. ",
    "server": "Place: a server room: dark navy walls, rows of tall black server racks with small green and orange lights. ",
    "writer": "Place: a home office: olive wall, a warm wood desk with a laptop, a full bookshelf, a green plant. ",
    "pizza": "Place: a small cosy pizza place: bottle-green wall, white tile counter, a brick oven glowing orange, red chairs, a green plant. ",
    "pizza_old": "Place: an old-fashioned pizza place from twenty years ago: wood panelling, a red-and-white checkered floor, a boxy old TV, a rotary phone on the counter. ",
    "office_nra": "Place: a quiet research office: cream wall, warm wood desk, filing cabinets in muted green, a green plant. ",
    "cityhall": "Place: a city hall chamber: dark-red wall, warm wood benches and a raised wooden desk, tall windows. ",
    "court": "Place: a courtroom in warm wood: a tall judge's bench, wooden benches, a cream wall, a tall window. ",
    "mall": "Place: a shopping mall hallway: cream floor tiles, teal shop fronts, big skylights, potted palms. ",
    "ghost": "Place: a cramped commercial kitchen in an alley: clay-red brick wall, steel shelves, many paper delivery bags on hooks, one stove. ",
    "studio": "Place: a bright video studio: purple wall, ring lights, cameras on tripods, a warm wood desk. ",
    "burger_brand": "Place: a shiny modern burger shop: bright blue wall, white counter, big windows, potted plant. ",
    "store": "Place: a small corner convenience store at night: bright white light, a teal counter, shelves of snacks in flat colours, a hot dog roller. ",
    "boardroom": "Place: a corporate boardroom: grey-blue wall, a long warm wood table, leather chairs, a big window over a city. ",
    "ballot": "Place: a polling place in a school gym: warm wood floor, cream walls, blue voting booths with small curtains. ",
    "home_driver": "Place: a small plain apartment: pale teal wall, a small wood table, a coat rack, a window with rain. ",
}
TINTS = ["The light is warm and golden. ", "The light is cool and bluish. ",
         "The light is warm and orange. ", "The light is cool and teal. "]
CLOSE_WORDS = ("seen close", "close view", "close-up")
WIDE_WORDS = ("wide view", "seen wide", "from above")


def sid(i):
    return "d%03d" % (i + 1)


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


def cast(what):
    w = what.lower()
    out, seen = [], set()
    for key, block in CAST:
        if key in w and block not in seen:
            out.append(block)
            seen.add(block)
    return "".join(out)


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
        if len(re.findall(r"raccoon", s["what"], re.I)) and "two raccoon" in s["what"].lower():
            errs.append("%s: два енота" % sid(i))
    n = sum(1 for _ in open(HERE / "script_delivery.txt", encoding="utf-8"))
    miss = sorted(set(range(1, n + 1)) - covered)
    if miss:
        errs.append("строки без кадра: %s" % miss)
    return errs


def main():
    if len(sys.argv) > 1:
        i = int(sys.argv[1].lstrip("d")) - 1
        print(prompt(i))
        return
    errs = check()
    for e in errs:
        print("ОШИБКА:", e)
    if errs:
        sys.exit(1)

    out, data, batch = [], [], 0
    flow = [i for i, s in enumerate(SHOTS) if s["mode"] != "chart"]
    out.append("ПРОМПТЫ ДЛЯ FLOW — «DoorDash Isn't the One Taking Your Money»")
    out.append("Nano Banana 2 · 16:9 · x1. Один промпт = одна картинка. Пачки по 10, после пачки скачать в 2K.")
    out.append("Имя файла при сохранении = номер кадра (d001.jpg …).")
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
    (HERE / "ПРОМПТЫ_доставка.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    (HERE / "prompts_delivery.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("готово: %d кадров, %d для Flow, %d схем, %d пачек" % (len(SHOTS), len(flow), len(SHOTS) - len(flow), batch))


if __name__ == "__main__":
    main()
