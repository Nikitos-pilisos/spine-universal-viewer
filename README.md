# Spine Universal Viewer

Просмотрщик Spine-анимаций с выбором рантайма: **3.7, 3.8, 4.0, 4.1, 4.2, 4.3** (автоопределение версии по файлу).
Spine animation viewer with runtime switching: **3.7, 3.8, 4.0, 4.1, 4.2, 4.3** (version auto-detected from the file).

## Запуск / Run
- **Десктоп / Desktop:** `pip install pywebview`, затем `python app.py`. Проекты (.json/.skel + .atlas + .png), положенные в папку плеера, подхватываются автоматически.
- **Браузер / Browser:** откройте страницу GitHub Pages и перетащите .json/.skel, .atlas и .png в окно.
- [Запустить Онлайн]([runtimes/LICENSE-spine-runtimes.txt](https://nikitos-pilisos.github.io/spine-universal-viewer/))

## Возможности / Features
- Навигация: перемещение мышью, зум колесом к курсору, Fit
- Debug: кости, сетка и hull мешей, region-рамки, bounding boxes, paths, clip-полигоны
- Статистика: FPS, draw calls, RAM, VRAM (оценка), вертексы/треугольники, вес JSON, атласа и графики
- Clipping-маски и backface culling — вкл/выкл
- **NLA-редактор:** дорожки, перетаскивание анимаций на таймлайн, кроссфейд наложением клипов, слои (вес / Additive), зум и прокрутка таймлайна, экспорт/импорт раскладки
- **NDA-режим:** в превью графика заменяется плейсхолдером «NDA Placeholder» (силуэт и UV сохраняются)
- Язык интерфейса: English / Русский — по языку системы, переключение флагами 🇺🇸 / 🇷🇺 в шапке
- **Свой фон (сцена):** загрузка изображения, перемещение и масштаб мышью, прозрачность — для проверки анимации в сцене
- **Ватермарка:** произвольный текст поверх превью (мозаика / центр / угол), размер, цвет, прозрачность, угол

Горячие клавиши: `Space` пауза, `F` fit, `B` кости, `M` меш, `C` clipping, `H` скрыть картинку, `N` NDA, `E` редактировать фон, `G` сетка, `S` статистика.

## Лицензия / License
Папка `runtimes/` содержит Spine Runtimes © Esoteric Software, распространяется по
[Spine Runtimes License](runtimes/LICENSE-spine-runtimes.txt). Для использования нужна действующая лицензия Spine Editor.
