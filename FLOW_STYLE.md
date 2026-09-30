# Flow: стиль и промпты для кадров

Выжимка из сессии «Higgsfield setup» (29–30.09), которая оборвалась на лимите.
Источник: переписка сессии (`flow_prompts.txt`). Код конвейера (`shots_*.py`, `prompt_*.py`)
лежит у тебя в `C:\Users\mrtay\Desktop\project\`, в переписку он попадал только кусками.

Пометки:
- **[точно]** текст взят из переписки дословно;
- **[по описанию]** в переписке был только пересказ, формулировка восстановлена.

---

## 1. Где остановились

- Канал **Dirty Margins**, ролик про доставку: **«DoorDash Isn't the One Taking Your Money»**.
- Текст для озвучки: 4544 слова, примерно 24–25 минут. Лежит в `Ютуб\Dirty Margins\озвучка\Доставка - текст для озвучки.txt`.
- Начало уже исправлено: «This burger costs fifteen dollars at the counter. Delivered to your door, the same burger costs thirty-eight. Here's how that happens.» Слово «Okay» в начале роликов больше не используем.
- Последнее сообщение: «Пишу список кадров для доставки: около 280 кадров на 424 строки текста». Этот список не дописан.
- Старый план на 368 кадров (`shots_del.py` + `shots_del_extra.py`) делался под прошлую версию сценария на 5009 слов. К новому тексту он подходит только частично.
- Потом: генерация во Flow, монтаж через **OpenMontage**. Сквозной приём ролика: **чек, который растёт по ходу ролика** («Your $32 order»); каждая глава добавляет в него строку. Чек рисуется поверх кадров, во Flow его генерировать не нужно.

---

## 2. Настройки Flow

- Режим «Изображение», **Nano Banana 2**, **16:9**, **x1** (0 кредитов).
- На Nano Banana 2 есть дневной лимит. На Pro/Lite не переключаемся: плывёт стиль, и Pro может тратить кредиты.
- Промпты отправлять по одному, пачками примерно по 10. Кнопку отправки нажимать кликом: Enter иногда теряет промпт.
- Качать в 2K: открыть картинку → скачать → «Повышенное разрешение». После примерно 25 скачиваний 2K подряд Flow тормозит; тогда брать 1K и увеличивать локально.
- Надпись «Flow ещё не работает в вашей стране» означает, что выключен VPN. Во время рендера Remotion Flow виснет или показывает чёрную страницу.
- Если в чате проекта застряли отменённые детали (енот с указкой и т. п.), создавай **новый проект**.
- Порядок файлов при скачивании не совпадает с порядком промптов: проверяй кадры по контактному листу.

---

## 3. Стиль кадров Dirty Margins

### 3.1 Короткий стилевой блок (шапка пачки) [точно]

```
Flat 2D cartoon illustration, thick black outlines, flat colours, no shading, no gradients. A friendly palette of flat real colours: soft teal, warm wood, cream, muted green, clay and grey-blue, never washed out and never grey all over. The room is calm, tidy and minimal: walls, floor, two or three large pieces of furniture and one green plant, and the wall, floor and furniture are NOT all the same colour. No crowd of small props, no busy detail. One single subject fills about half the frame in the strongest colour. Nobody in the shot at all unless the shot says otherwise.
```

### 3.2 Палитра (часть BASE) [точно]

```
A friendly palette of flat, real colours — soft teal, warm wood, cream, muted green, clay and grey-blue — never washed out and never grey all over. The one subject of the shot carries the strongest and warmest colour in the frame.
```

### 3.3 Комната, предмет, люди [по описанию]

- **ROOM_LOOK:** комната спокойная, аккуратная, минимальная. Стена, пол и мебель НЕ одного цвета: минимум три разных плоских цвета плюс растение или другое «живое» пятно.
- **SUBJECT:** один главный предмет примерно на половину кадра, самый сильный цвет и самый высокий контраст.
- **PEOPLE:** «One to three people in the shot, only the ones named below…» В кадре только те, кто назван в описании.
- **Цвет в каждой комнате прописывать явно**, это главный рычаг. Примеры из прошлых роликов: кухня с бирюзовой плиткой, кремовыми шкафами и деревянной столешницей; архив с оливковой стеной; библиотека с тёмно-красной стеной; гостиная с пыльно-розовой стеной и горчичным диваном.
- Крупность кадра меняй (общий / средний / крупный), и в соседних кадрах должен быть разный предмет. Иначе получается «одна комната с разных ракурсов».

### 3.4 Текст в кадре

Без надписи [точно]:
```
NO TEXT, no letters, no numbers, no signs, no labels anywhere in the image. No brand logos.
```

С надписью на предмете (BAKE_LINE) [точно]. Вместо первого `%s` подставляется стиль надписи, вместо второго сама надпись:
```
Written large across the main object of this shot, %s, is this and nothing else: %s. Spell it exactly like that. The lettering is big enough to read at a glance, taking up a large part of the frame, even if the object it is on has to be drawn bigger or closer. There is no other writing anywhere in the picture.
```

Стиль надписи:
- слова: `in clean bold black capitals` [точно]. «Hand-lettered» получается кривым, его не используем;
- цифры цветные [по описанию]: красные с обводкой или белые на красной/бирюзовой табличке.

Правила:
- надпись ≤ 3–4 слов или одно число, и только на предмете в сцене (чек, табличка, ценник). Поверх кадра текст не кладём;
- **одно значение на предмет**. Два числа на одном листе сливаются; для сравнения делай отдельную карточку на каждый предмет или схему в монтаже;
- если описание содержит «seen close», кадр идёт крупным планом; кадры с надписью в помещении — средним;
- объект с надписью называй крупным: «large sign / board / tag / receipt»;
- выдуманные суммы в описании заменяй словами. Реальные цифры из сценария рисуются схемами в монтаже.

### 3.5 Персонажи

Енот-маскот [точно]. Роль в первой фразе меняется под сцену (mechanic, seller, courier…):
```
The mechanic in this scene is the channel mascot: a cartoon raccoon standing upright like a person, black bandit mask across the eyes, large white eyes, a sly narrow-eyed grin, wearing a dark green shop apron over a white shirt with rolled sleeves. Exactly the same raccoon design every time.
```

Глаза енота (добавлять всегда вместе с ним) [точно]:
```
His eyes are NOT the round friendly eyes used elsewhere in this style: they are narrowed to sly slits, half-closed, with the mouth curled up on one side in a crafty, scheming smile.
```

Клиент в сером пальто, «ты» в ролике [точно]:
```
The customer in this scene is the channel's second recurring character: a simple cartoon person, plain round head, short reddish-brown hair, large round white eyes with small black pupils, wearing a grey coat over a cream sweater. Exactly the same design every time.
```

Правила по персонажам:
- в описании кадра всегда пиши «the raccoon …» и «the customer in the grey coat». По этим словам подставляются блоки выше; с дефисом «grey-coat» тоже подставлять;
- **только один енот** в кадре;
- там, где енот забирает деньги или обманывает, лицо хитрое: «a sly, knowing half-smile»;
- персонаж стоит в сцене, а не у края кадра;
- не просить модель считать («exactly five dots»): она ошибается. Вместо чисел называй места («one on the west coast, one in the middle…»);
- фильтр Flow блокирует сцены, где кто-то кого-то физически удерживает. Пиши нейтрально.

### 3.6 Порядок сборки промпта [точно]

```
STYLE → ROOM_LOOK (или FLAT) → SUBJECT → PEOPLE → (BAKE_LINE или NOTEXT)
      → ROOMS[room] + ракурс → оттенок (тёплый/холодный по очереди) → крупность → описание кадра
```
К описанию добавляются блоки COON + COON_EYES, если в нём есть «raccoon», и CUST, если есть «grey coat».

### 3.7 Формат пачки из трёх кадров (если слать тройками) [точно]

```
Generate THREE separate 16:9 images...

Style for all of them: <блок 3.1>

IMAGE ONE: <промпт кадра без стилевой шапки>

IMAGE TWO: ...

IMAGE THREE: ...

Generate only these 3 images, nothing else.
```

---

## 4. Для ролика про доставку

- Енот — сторона, которая забирает деньги: приложение или курьер с пачкой денег, в зелёном фартуке. Клиент в сером пальто — тот, кто платит.
- Для превью намечено: «THE DIRTY DELIVERY TRICK», енот-курьер с пачкой денег, девушка с пакетом еды, цифры $32 ORDER / 29¢ PROFIT / 30% COMMISSION / $14.62 TO RESTAURANT / $7 DRIVER.
- Цифры (29¢, $4.32, 15/25/30%, $7.3B → $650M и т. д.) идут схемами в монтаже, во Flow их не генерируем.

---

## 5. Для справки: Danger Premium

Стиль тот же: плоский 2D-мультфильм, толстые чёрные контуры. Енот одет по теме ролика; в Антарктиде это была красная парка и оранжевая каска. Промпты шлются по одному, пачками по 10, качаются в 2K.
