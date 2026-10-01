Nuclear Plants Hired Him for 12 Minutes — монтаж через OpenMontage (remotion-composer, композиция Explainer)

frames/            124 кадра n001…n132.jpg (номера с пропусками: пропущенные номера — схемы с цифрами)
voice.mp3          озвучка
montage_nuclear.json  файл монтажа для Explainer: кадры по таймингу озвучки, 8 схем, счётчик дозы, звук
frames_nuclear.csv    тайминг каждого кадра (начало, длительность, строки сценария)
openmontage_patch/    доработки OpenMontage: счётчик дозы (DoseCounter), исправленный Explainer.tsx,
                      заглушки шрифтов (нужны только без доступа к Google Fonts)

Как собрать у себя:
1. В папке OpenMontage/remotion-composer скопировать содержимое openmontage_patch/src в src/
   (fontshim не обязателен; если не копировать — верните в Explainer.tsx импорт "@remotion/google-fonts/SpaceGrotesk").
2. Скопировать frames/*.jpg и voice.mp3 в remotion-composer/public/nuclear/
3. npx remotion render src/index.tsx Explainer out/nuclear.mp4 --props=montage_nuclear.json
