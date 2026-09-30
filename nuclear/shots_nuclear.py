# -*- coding: utf-8 -*-
"""Раскладка кадров: Danger Premium, «Nuclear Plants Hired Him for 12 Minutes».

S(a, b, room, what, txt) — кадр под строки a..b сценария (script_nuclear.txt, с 1).
Если несколько кадров стоят на одной строке, gen_timing_nuclear.py делит её время поровну.
Теги персонажей в what: "the raccoon", "the raccoon in the yellow suit", "the timekeeper".
C(a, b, label) — схема для монтажа, во Flow не генерируется.
Счётчик дозы в углу рисуется в монтаже поверх всех кадров.
"""

SHOTS = []


def S(a, b, room, what, txt=""):
    SHOTS.append(dict(a=a, b=b, room=room, what=what, txt=txt, mode="bake" if txt else ""))


def C(a, b, label):
    SHOTS.append(dict(a=a, b=b, room="", what=label, txt="", mode="chart"))


# ---------------------------------------------------------------- ХУК 1–14
S(1, 2, "platform", "The raccoon in the yellow suit standing on a steel platform, looking up at a small round dark hole in a huge curved steel wall just above his head, seen from below.")
S(1, 2, "platform", "A small round manway hole in a giant curved steel tank, seen close: an open empty dark hole with no door, no cover and no lid, a thin green glow at its rim, the opening barely wider than a car tyre.")
S(3, 3, "platform", "The raccoon in the yellow suit seen full length from the front, arms slightly out, the suit puffed up with air, a thick air hose running from his back.")
S(3, 3, "platform", "The timekeeper standing beside the raccoon in the yellow suit, holding up a big silver stopwatch with his thumb on the button.")
S(4, 4, "plant", "Wide view of a nuclear power plant at dusk, two big cooling towers with white steam, a domed reactor building beside them.")
S(4, 4, "cutaway", "A simple cutaway drawing of a giant steel steam generator tank as tall as a five-storey building, shaped like a very tall capsule standing upright, its outer wall cut away to show thousands of thin vertical tubes inside and a rounded bowl at the very bottom glowing faint green. At its foot, tiny next to it, the raccoon in the yellow suit stands on a small steel platform looking up. Wide view, the whole tank fits in the frame.")
S(5, 5, "bowl", "Inside a dark curved steel dome, the walls glowing a sickly green, faint wavy lines of radiation drifting in the air.")
S(6, 6, "office", "A big paper wall calendar whose grid is only empty squares with no printed words or numbers, a huge red marker ring drawn around the whole grid, and the text written in thick red marker inside the ring, seen close.", "5 REM")
S(7, 7, "platform", "The timekeeper's big silver stopwatch seen close, a plain dial with no numbers, and a white paper tag tied to the stopwatch with the text printed on the tag.", "12 MIN")
S(8, 8, "platform", "The raccoon in the yellow suit looking at a big wall calendar whose pages are flying off one after another.")
S(9, 9, "platform", "The raccoon in the yellow suit climbing up a short ladder into the round manway hole above him, arms raised, his helmet and shoulders already inside the opening, his yellow boots on the top rung, the air hose trailing behind.")
S(9, 9, "bowl", "Inside the dark steel bowl, the raccoon in the yellow suit pushing a heavy round metal plug into a big pipe opening with both arms.")
S(10, 10, "locker", "Three workers in yellow plastic suits standing in a row in a changing room, helmets under their arms, all looking at the viewer.")
S(11, 11, "locker_old", "A 1970s locker room, workers in white paper coveralls laughing, a faint cartoon green glow drawn around one of them as a joke.")
S(12, 12, "platform", "The raccoon in the yellow suit tapping a small dosimeter clipped to his chest, looking at the viewer.")
S(13, 13, "home", "An ordinary living room with a sofa, a bowl of bananas, a window with sunshine and a stone wall outside, all glowing very faintly, a relaxed family reading.")
S(13, 13, "platform", "The raccoon in the yellow suit pointing with one gloved paw at the top corner of the picture, looking at the viewer.")
S(14, 14, "plant", "The raccoon in an orange work jacket standing at the plant gate at night, lights of the reactor behind him.")
S(14, 14, "platform", "The round manway hole seen from below with the raccoon's paw reaching up toward it.")
S(14, 14, "plant", "Two cooling towers and a small crowd of workers in coveralls walking toward the plant in the morning light.")

# ---------------------------------------------------------------- КАК УСТРОЕНО 15–26
S(15, 15, "plant", "Wide view of a 1970s nuclear plant under construction, cranes, a half-built cooling tower, workers in hard hats.")
S(15, 15, "cutaway", "A simple diagram-like cutaway of a nuclear plant: a reactor on the left, a tall tank in the middle, a turbine on the right, two separate loops of pipe, one red and one blue.")
S(16, 16, "cutaway", "The red loop of pipe glowing, hot water flowing out of the reactor core, small glowing green specks carried along in it.")
S(17, 17, "cutaway", "A tall steel steam generator tank drawn cut open, thousands of thin U-shaped tubes packed inside it.")
S(17, 17, "turbine", "A huge turbine hall, a big turbine spinning, white steam curling from a pipe.")
S(18, 18, "bowl", "The curved bottom chamber of the steam generator seen from inside, a flat steel ceiling above full of thousands of small tube holes, two big round pipe openings in the walls.")
S(19, 19, "cutaway", "Close view of the inside of a pipe, tiny grey metal flakes drifting with the water and turning glowing green as they pass the reactor core.")
S(19, 19, "bowl", "The walls of the steel bowl coated with a dark crusty layer, glowing faintly green.")
S(20, 20, "bowl", "One tiny glowing speck on the bowl wall seen close, sharp rays shooting out of it in every direction.")
S(21, 21, "control", "A control room during a shutdown, operators turning big switches, a large panel of lights going dark.")
S(21, 21, "bowl", "Wide view of the empty glowing bowl, the manway hole a bright circle on the wall.")
S(22, 22, "platform", "The raccoon in the yellow suit climbing the last rungs of a steel ladder toward the platform.")
S(23, 23, "pool", "A deep blue refueling pool above a reactor, a big crane holding a long fuel assembly underwater, workers on a bridge above.")
S(23, 23, "platform", "Workers in suits opening a big round hatch on the side of the steam generator, bolts on the floor.")
S(24, 24, "bowl", "A big round pipe opening in the bowl wall, and next to it a heavy round metal plug with a rubber rim waiting to be fitted, seen close.")
S(25, 25, "bowl", "A robot arm with a camera and clamps reaching into the bowl through the manway, its little work light shining.")
S(26, 26, "bowl", "The raccoon in the yellow suit's gloved paws tightening a big bolt on the round plug, seen close.")

# ---------------------------------------------------------------- ЛИМИТ 27–37
S(27, 27, "office", "A small black dosimeter badge clipped to a work jacket, seen close.")
S(27, 27, "office", "A tall steel filing cabinet with one drawer open, full of paper folders, the raccoon in an orange work jacket pulling out one folder.")
C(28, 28, "до 1994: 3 rem за квартал, пожизненно не больше 5 × (возраст − 18)")
C(29, 29, "с 1994: 5 rem в год")
C(30, 30, "5 rem = 50 mSv  vs  средний американец ≈ 6 mSv в год")
S(31, 31, "clinic", "A doctor's office with a chest X-ray on a lightbox, a patient in a gown.")
C(32, 32, "1 год на лимите ≈ 8 лет обычной жизни ≈ 2 500 рентгенов")
S(33, 33, "office", "The plant manager, a simple cartoon man in a tie and short sleeves, sitting behind a desk covered in papers, looking straight at the viewer.")
S(34, 34, "office", "A trained technician in a blue uniform sitting on a bench with nothing to do, his dosimeter glowing red, his coworkers busy behind him.")
S(35, 35, "office", "The plant manager drawing a big red cross over a small photo of the technician pinned on a board.")
S(36, 36, "office", "The plant manager shaking hands with a new temporary worker in white coveralls at the door, a thin empty folder in the manager's other hand.")
S(36, 36, "office", "An empty paper folder open on the desk, seen close, one blank page inside.", "0 REM")
S(37, 37, "office", "The plant manager holding up the empty folder and smiling.")

# ---------------------------------------------------------------- КТО ПРЫГАЛ 38–54
S(38, 38, "gate_old", "A long line of men in 1970s clothes waiting at a nuclear plant gate at dawn, lunch boxes in their hands.")
S(39, 39, "floor_old", "Workers in white paper coveralls mopping a concrete floor with buckets, a yellow-and-magenta rope around the area.")
S(39, 39, "floor_old", "A worker in white coveralls rolling a steel drum with a radiation trefoil symbol on it.")
S(40, 40, "locker_old", "Regular staff in blue uniforms pointing and grinning at a group of temporary workers in white paper coveralls.")
S(41, 41, "newsroom", "A freelance journalist with a moustache at a desk piled with government reports, typing on a typewriter.")
S(42, 42, "control", "A big electricity meter on a 1970s control panel, its needle slowly dropping, seen close.")
C(42, 42, "1978 → 1980: выработка ↓, облучаемых 44 000 → 77 000")
S(43, 44, "floor_old", "A crowd of many temporary workers in white coveralls squeezed into one room, each holding a tiny dosimeter.")
S(45, 45, "road_old", "An old pickup truck driving on a highway at night past a road junction, a cooling tower far behind and another one far ahead.")
S(46, 46, "motel", "A worker in a plain white T-shirt sitting on the edge of a cheap motel bed, looking at a pay envelope.")
S(47, 47, "motel", "The same worker counting cash on the motel bedspread, a beach postcard stuck in the mirror frame.")
S(47, 47, "beach", "The worker lying on a sunny beach under an umbrella, a cooling tower tiny on the horizon.")
S(48, 48, "motel", "The worker handing a folded pile of cash to his landlady at an apartment door.")
S(49, 49, "mockup", "A mechanical engineer in a white hard hat raising his hand to volunteer in front of a small group.")
S(50, 50, "plant", "Wide view of a nuclear plant on a rocky California coast, blue ocean, a domed reactor building on the cliffs.")
S(50, 50, "mockup", "A mechanical engineer in a yellow bubble suit and clear round helmet standing next to a full-size model of the bottom of a steam generator.")
S(51, 51, "mockup", "The engineer in the yellow suit climbing a ladder to a platform under a round hole in the model.")
S(51, 51, "mockup", "The engineer in the yellow suit with both arms raised above his head, pushing himself up headfirst into the round hole of the model.")
S(52, 52, "mockup", "A heavy bolt falling from a gloved hand inside the model, seen close, slow motion lines around it.")
S(53, 53, "bowl", "A long orange robot arm unfolding inside the steel bowl, a camera on its end.")
S(53, 53, "control", "Technicians in a trailer watching the robot arm on small TV screens, one holding a joystick.")
S(54, 54, "bowl", "The robot arm stuck with a jammed claw, a spark flying from it.")
S(54, 54, "mockup", "A new class of young workers in yellow suits lined up in front of the model for training.")

# ---------------------------------------------------------------- ЯПОНИЯ 55–69
S(55, 55, "japan_map", "A simple map of Japan drawn on paper, a small cooling tower icon on its east coast.")
S(56, 56, "japan_desk", "A Japanese writer with glasses at a low wooden desk writing a book by hand, a pile of pages beside him.")
S(56, 56, "japan_desk", "The writer's hand holding an old photo of contract workers in coveralls standing outside a Japanese nuclear plant, seen close.")
S(57, 57, "japan_desk", "A thin paperback book lying on the desk with a cartoon worker in coveralls on its cover.")
S(58, 58, "yoseba", "A day-labor corner at dawn in a Japanese city, a crowd of men in work clothes waiting by a road, a van pulling up.")
S(59, 59, "fukushima", "Wide view of a coastal nuclear plant with damaged reactor buildings, white smoke rising, the sea behind.")
S(60, 60, "fukushima", "A worker in a white full-body protective suit and gas mask walking toward a damaged reactor building.")
S(60, 60, "fukushima", "A thick envelope of yen banknotes held out toward the viewer, seen close.", "¥200,000")
S(61, 61, "japan_room", "A young Japanese man of twenty-seven sitting at a small table, looking at a phone with a surprised face.", "¥400,000")
S(62, 62, "japan_room", "A reporter with a notebook interviewing a tired worker in a small apartment kitchen.")
S(62, 62, "fukushima", "A line of more than thirty workers in white suits, only one of them holding a full envelope of money.")
S(63, 63, "japan_room", "A paper payslip on a table, seen close, one small line on it circled in red.", "$36")
S(64, 64, "fukushima", "Wide view of a Japanese countryside, workers in white suits shovelling soil into big black bags that stand in long rows.")
S(65, 65, "sendai", "A Japanese train station at dawn, a man in a dark jacket walking between homeless men sleeping on cardboard.")
S(65, 65, "sendai", "The man in the dark jacket handing a small bill to a van driver while two homeless men climb into the van.", "$100")
S(66, 66, "fukushima", "Homeless men in cheap white suits shovelling radioactive soil into black bags.")
S(66, 66, "fukushima", "A tall stack of four company signboards on posts, each smaller one below the bigger one, a tiny worker at the very bottom.")
S(66, 66, "japan_room", "A worker in a bare dormitory room eating a small bowl of rice, a list of deductions pinned on the wall.")
S(67, 67, "chernobyl", "Wide view of a ruined reactor building with a smashed roof, grey sky, 1986.")
S(68, 68, "chernobyl", "A small tracked robot stopped dead on the roof among black chunks of debris, smoke from its electronics.")
S(68, 68, "chernobyl", "Soviet soldiers in home-made lead aprons and gas masks running across the roof with shovels.")
S(69, 69, "cutaway", "Three small pictures side by side: an American jumper in a yellow suit, a Japanese worker in a white suit, a Soviet soldier with a shovel.")
S(69, 69, "platform", "A new worker in a yellow suit holding a thin empty folder, walking toward the glowing round hole.")

# ---------------------------------------------------------------- ЗДОРОВЬЕ 70–79
S(70, 70, "locker", "The raccoon in the yellow suit sitting on a bench in the changing room after a jump, helmet off, breathing hard.")
S(71, 72, "locker", "The raccoon in an orange work jacket walking out of the plant gate feeling fine, stretching his arms.")
S(72, 72, "home", "The raccoon in an orange work jacket at home brushing his fur in the mirror, nothing wrong with him.")
S(73, 73, "home", "An hourglass on a shelf, the sand running slowly, the raccoon's shadow in the background.")
S(74, 74, "study", "A thick medical journal lying open on a desk with charts on the pages.")
S(75, 75, "study", "Three flags on small poles on a research desk: France, the United Kingdom and the United States, a mountain of paper files behind them.")
S(75, 75, "study", "A researcher in glasses scrolling through a very long list of names on a computer screen.")
S(76, 76, "study", "A researcher pointing at a hand-drawn line on a whiteboard that rises slowly from left to right.")
C(76, 76, "INWORKS: риск растёт вместе с дозой, даже ниже лимитов")
C(77, 77, "1 год на лимите ≈ +2–3 % к риску смерти от рака")
S(78, 78, "platform", "The raccoon in the yellow suit shrugging on the platform, one small jump drawn as a tiny dot on a long wall chart behind him.")
S(79, 79, "office", "The same worker's folder getting thicker and thicker as new pages are stapled onto it, seen close.")
S(79, 79, "road_old", "A pickup truck driving on a long highway past one cooling tower after another.")

# ---------------------------------------------------------------- СЕГОДНЯ 80–90
S(80, 80, "plant_tmi", "Wide view of a nuclear plant on an island in a wide river, two tall cooling towers, today.")
S(81, 81, "plant_tmi", "The same plant with a chain across its gate and dark windows, grass growing, 2019.")
S(82, 82, "datacenter", "A huge modern data center with rows of glowing server racks, power lines running to it from the distance.")
S(82, 82, "plant_tmi", "A handshake over a long table between a power company boss and a tech company boss, a plant model on the table.")
S(83, 83, "plant_tmi", "Workers repainting the plant, a new clean sign board on the gate with no letters on it, cranes and trucks around.")
S(83, 83, "office", "A wall calendar in a site office with one year circled, a hard hat hanging next to it, seen close.", "2027")
S(84, 84, "plant_mi", "A nuclear plant on the sandy shore of a big lake in Michigan, one domed building, lights coming back on.")
S(85, 85, "gate", "A modern plant parking lot at dawn full of pickup trucks and campers with licence plates from many states, workers carrying gear to the gate.")
S(85, 85, "road_old", "A line of modern pickup trucks towing small campers along a highway at dawn toward two cooling towers.")
S(86, 86, "laptop", "A laptop on a motel table showing a job board page with many job cards, seen close.", "$23–73/HR")
S(86, 86, "motel", "A contract worker in a modern hi-vis jacket packing a duffel bag in a motel room, a truck outside the window.")
S(87, 87, "gate", "Contract workers in hard hats doing ordinary jobs: carrying scaffolding, checking a clipboard, painting a rail.")
S(88, 88, "locker", "Modern workers in coveralls queuing at a counter to hand in their small dosimeter badges.")
C(88, 88, "2023: 93 489 под контролем, средняя доза ≈ 0,16 rem")
S(89, 89, "bowl", "A modern robot arm working alone inside the steel bowl, thick shielding walls outside, a clean bright light.")
S(90, 90, "platform", "The raccoon in the yellow suit standing again on the platform under the round hole, looking up.")
S(90, 90, "office", "The plant manager opening a thin empty folder again, a new name on the tab hidden by his thumb.")

# ---------------------------------------------------------------- ФИНАЛ 91–96
S(91, 91, "platform", "Close view of the raccoon in the yellow suit's face behind the clear helmet, his eyes wide.")
S(92, 92, "bowl", "The raccoon in the yellow suit alone inside the glowing bowl, sitting on the curved floor, the stopwatch hanging on his wrist.")
S(92, 92, "platform", "The timekeeper staring at his stopwatch in shock, the hand spun far past twelve.")
S(93, 93, "office", "The plant manager handing the raccoon in an orange work jacket an envelope of pay and pointing at the exit door.")
S(94, 95, "platform", "The raccoon in the yellow suit turning to the viewer from the platform, one paw pointing up at the round hole.")
S(96, 96, "platform", "The round manway hole seen from below, dark and quiet, the empty platform under it.")


if __name__ == "__main__":
    n = len(SHOTS)
    c = sum(1 for s in SHOTS if s["mode"] == "chart")
    print("кадров:", n, "| Flow:", n - c, "| схем:", c)
