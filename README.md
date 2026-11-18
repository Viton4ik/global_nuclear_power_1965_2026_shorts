# ☢️ Nuclear Power Race: Global Atomic Electricity Generation (1965 – Oct 2026) | Cherenkov 3D Edition
# ☢️ Атомная гонка: Выработка электроэнергии на АЭС по странам (1965 – Окт 2026) | Cherenkov 3D

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Format 9:16 MP4](https://img.shields.io/badge/Output-1080x1920%20MP4%20(30%20FPS)-00f5d4.svg)
![Audio CC0](https://img.shields.io/badge/Audio-CC0%201.0%20Public%20Domain-success.svg)

**[English](#english)** | **[Русский](#русский)**

---

## 🖼️ Visual Preview / Превью кадров (2005 vs 2026)

| **2005: Pre-Fukushima & German Peak / Пик Японии и Германии** | **2026: China's Surge & German Exit / Рывок Китая и выход Германии** |
| :---: | :---: |
| ![2005 Preview](previews/preview_2005.png) | ![2026 Preview](previews/preview_2026.png) |

---

<a name="english"></a>
## 🇬🇧 English

### Overview
An automated, self-contained Python pipeline that renders a **40-second vertical HD (9:16, 1080x1920, 30 FPS) MP4 video** with an atmospheric sci-fi Cherenkov soundtrack. It visualizes the dramatic historical evolution of **Annual Nuclear Electricity Generation by Country (in Terawatt-hours, TWh)** from **1965 to October 2026** based on **IAEA PRIS (Power Reactor Information System)** and **World Nuclear Association** statistics.

### Historical Drama & Key Turning Points
* **Early Pioneers (1965–1975):** The United States, the United Kingdom, and the USSR launch the world's first commercial nuclear grids.
* **France's Historic Bet (1980s–2000s):** Following the oil crises, France executes the Messmer Plan, surging to #2 globally and generating over 70% of its electricity from nuclear power.
* **Japan's Rise & 2011 Fukushima Shock:** Japan climbs to #3 in the world (~320 TWh), then drops to zero in 2014 after the Fukushima Daiichi accident before gradually restarting reactors through 2026.
* **Germany's Complete Phase-Out (`Atomausstieg`):** Once the world's #4 nuclear producer (~170 TWh in 2000), Germany progressively shuts down its fleet and exits the ranking completely in April 2023.
* **21st-Century Asian & Eurasian Surge (2015–2026):** China overtakes Germany, Japan, Russia, South Korea, and France to claim #2 globally (455 TWh), alongside strong expansion in Russia, South Korea, India, and the UAE.

### Key Visual & Technical Features
* **"Cherenkov Radiation 3D" Aesthetic:** Deep abyssal reactor-pool background (`#030914` / `#061224`) paired with smooth, translucent-looking 3D fuel-rod capsules glowing from deep indigo-cobalt (`#1e1b4b`) to dazzling Cherenkov aquamarine and neon turquoise (`#00f5d4` / `#99f6e4`).
* **Reactive Reactor State Gradients (`▲` / `▼`):**
  * **Reactor Expansion (`▲`):** Rapid nuclear capacity additions intensify the luminous turquoise-white Cherenkov glow at the capsule tip.
  * **Reactor Shutdown / Phase-Out (`▼`):** Sharp output reductions shift the capsule tip toward a warning rose-amber cooldown hue (`#fda4af`).
* **Quantum Particle & Ionization Wave Animations:** Floating Cherenkov quantum particles pulse in the reactor pool background, while a travelling ionization wave glides along each 3D capsule.
* **Royalty-Free Sci-Fi Soundtrack (`CC0 1.0`):** Automatically synthesizes a 40-second stereo track (*"Cherenkov Quantum Resonance"* — deep reactor magnetic hum, shimmering glass pads, and crystalline quantum pulse arpeggios) with a `MUSIC_LICENSE_CC0.txt` certificate.
* **Zero System Clutter (Auto-Venv & Self-Cleanup):** `run.py` automatically creates a temporary `.venv_nuclear_race` virtual environment, installs all required packages (including a portable `FFmpeg` binary via `imageio-ffmpeg`), renders the final `.mp4`, and removes the virtual environment and temporary files upon completion (preserving `previews/` for GitHub).

### Quick Start
1. Ensure **Python 3.8+** is installed on your machine.
2. Clone this repository or extract the project archive.
3. Run the generator with a single command:
   ```bash
   python run.py
   ```
   *(On macOS/Linux, you may use `python3 run.py`)*.

### Repository Structure & Output Files
* `run.py` — Self-contained 3D video & audio generator script (100% English codebase).
* `previews/preview_2005.png` & `previews/preview_2026.png` — High-resolution 9:16 frame previews for GitHub documentation.
* `global_nuclear_power_1965_2026_shorts.mp4` — Final 40-second 1080x1920 vertical video with audio (generated upon running `run.py`).
* `MUSIC_LICENSE_CC0.txt` — Public Domain (CC0 1.0) license certificate for the audio track.
* `YOUTUBE_DESCRIPTION.txt` — Ready-to-use title, description, data sources, and tags for social media publishing.

---

<a name="русский"></a>
## 🇷🇺 Русский

### Описание проекта
Полностью автономный генератор на Python, создающий **40-секундный вертикальный видеоролик высокой четкости (9:16, 1080x1920, 30 FPS) в формате `.mp4`** с атмосферным научно-фантастическим саундтреком. Видео наглядно демонстрирует драматическую историю **выработки электроэнергии на АЭС по странам мира (в тераватт-часах, TWh)** с **1965 по октябрь 2026 года** по данным базы **МАГАТЭ (IAEA PRIS)** и **World Nuclear Association**.

### Драматургия и ключевые повороты истории
* **Старт первых реакторов (1965–1975):** США, Великобритания и СССР запускают первые промышленные атомные энергоблоки.
* **Историческая ставка Франции на мирный атом:** Реализация «плана Мессмера» выводит Францию на уверенное 2-е место в мире.
* **Взлет Японии и шок Фукусимы (2011):** Выход Японии в топ-3 мировых лидеров (~320 TWh), резкая остановка всех реакторов после аварии 2011 года и постепенный перезапуск к 2020–2026 годам.
* **Полный выход Германии из рейтинга (2023):** Германия, занимавшая 4-е место в мире (~170 TWh в 2000 году), поэтапно закрывает свои АЭС и полностью покидает рейтинг к апрелю 2023 года.
* **Стремительный рывок Китая, России и Южной Кореи (2015–2026):** Китай обгоняет Германию, Японию, Россию, Южную Корею и Францию, выходя на 2-е место в мире (455 TWh).

### Ключевые визуальные и технические особенности
* **Эстетика «Cherenkov Radiation 3D»:** Глубокий темно-лазурный фон реакторного бассейна (`#030914` / `#061224`) и гладкие полупрозрачные 3D-капсулы с эффектом свечения Черенкова (перелив от глубокого индиго к ослепительному аквамарину и неоновой бирюзе `#00f5d4`).
* **Реактивный градиент состояния реакторов (`▲` / `▼`):**
  * **Ввод новых энергоблоков (`▲`):** При быстром росте генерации вершина капсулы разгорается ярким бирюзово-белым черенковским свечением.
  * **Остановка реакторов (`▼`):** При резком сбросе генерации (Япония после 2011 г., Германия при закрытии АЭС) вершина капсулы окрашивается в предупреждающий розово-янтарный оттенок (`#fda4af`).
* **Анимация квантовых частиц и волны ионизации:** На фоне плавно пульсируют и поднимаются квантовые частицы в воде реакторного бассейна, а вдоль каждой 3D-капсулы пробегает волна ионизации.
* **Лицензионно чистая музыка (`CC0 1.0`):** Скрипт процедурно синтезирует 40-секундную стереодорожку (*«Cherenkov Quantum Resonance»* — глубокий магнитный гул реактора, переливающийся стеклянный пэд и кристальное квантовое арпеджио) и создает сертификат `MUSIC_LICENSE_CC0.txt`.
* **Полная самоочистка (Auto-Venv & Cleanup):** При запуске `run.py` сам создает изолированную виртуальную среду `.venv_nuclear_race`, скачивает внутрь все библиотеки и портативный видеокодек `FFmpeg` (`imageio-ffmpeg`), собирает готовый `.mp4` и автоматически удаляет виртуальную среду и временные файлы после завершения (сохраняя папку `previews/` для GitHub).

### Быстрый запуск
1. Убедитесь, что у вас установлен **Python 3.8+**.
2. Склонируйте репозиторий или распакуйте архив проекта.
3. Запустите генерацию одной командой в терминале (PowerShell / Bash):
   ```bash
   python run.py
   ```
   *(На macOS / Linux может использоваться команда `python3 run.py`)*.

### Структура репозитория и итоговые файлы
* `run.py` — автономный скрипт генерации 3D-видео и аудио (весь код внутри на английском языке).
* `previews/preview_2005.png` и `previews/preview_2026.png` — превью кадров высокого разрешения для витрины GitHub.
* `global_nuclear_power_1965_2026_shorts.mp4` — готовый 40-секундный вертикальный видеоролик со звуком (создается после запуска `run.py`).
* `MUSIC_LICENSE_CC0.txt` — сертификат свободной лицензии (CC0 1.0 Public Domain) на музыкальную дорожку.
* `YOUTUBE_DESCRIPTION.txt` — готовые заголовки, описание, источники и теги для загрузки на YouTube / Reels / TikTok.
