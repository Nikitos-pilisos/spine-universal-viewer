# Spine Universal Viewer

Просмотрщик Spine-анимаций с выбором рантайма: **3.7, 3.8, 4.0, 4.1, 4.2, 4.3** (автоопределение версии по файлу).

## Запуск
- **Десктоп:** `pip install pywebview`, затем `python app.py`. Проекты (.json/.skel + .atlas + .png), положенные в папку плеера, подхватываются автоматически.
- **Браузер:** откройте страницу GitHub Pages и перетащите .json/.skel, .atlas и .png в окно.

## Возможности
- Навигация: перемещение мышью, зум колесом к курсору, Fit
- Debug: кости, сетка и hull мешей, region-рамки, bounding boxes, paths, clip-полигоны
- Статистика: FPS, draw calls, RAM, VRAM (оценка), вертексы/треугольники, вес JSON, атласа и графики
- Вкл/выкл clipping-масок, backface culling
- Атласы с индексами (`Smoke` index:1 → `Smoke_1`)

Горячие клавиши: `Space` пауза, `F` fit, `B` кости, `M` меш, `C` clipping, `H` скрыть картинку, `G` сетка, `S` статистика.

## Лицензия
Папка `runtimes/` содержит Spine Runtimes © Esoteric Software, распространяется по
[Spine Runtimes License](runtimes/LICENSE-spine-runtimes.txt). Для использования нужна действующая лицензия Spine Editor.
