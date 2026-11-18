import os
import sys
import subprocess
import shutil
import venv

VENV_DIR = ".venv_nuclear_race"
TEMP_DIR = ".temp_nuclear_assets"


def create_venv():
    if not os.path.exists(VENV_DIR):
        print("[1/5] Creating isolated virtual environment (.venv_nuclear_race)...")
        venv.create(VENV_DIR, with_pip=True)


def get_venv_python():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    return os.path.join(VENV_DIR, "bin", "python")


def run_bootstrap():
    print("=====================================================================")
    print("  3D VIDEO GENERATOR: GLOBAL NUCLEAR POWER RACE (1965 - 2026)        ")
    print("=====================================================================")

    os.makedirs(TEMP_DIR, exist_ok=True)
    create_venv()
    venv_python = get_venv_python()

    print("[2/5] Installing required libraries and portable FFmpeg into virtual environment...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    subprocess.check_call([
        venv_python, "-m", "pip", "install",
        "pandas", "numpy", "matplotlib", "requests", "pillow", "imageio-ffmpeg", "-q"
    ])

    try:
        print("[3/5] Launching Cherenkov 3D rendering, audio synthesis, and MP4 assembly...")
        subprocess.check_call([venv_python, os.path.abspath(__file__), "--worker"])
    finally:
        print("[4/5] Self-cleanup: removing virtual environment and temporary assets...")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        print("[5/5] Cleanup complete! Final MP4 video and license files are ready in the project folder.")


def create_cherenkov_flag(code, width=80, height=52, radius=10):
    from PIL import Image, ImageDraw
    import numpy as np

    canvas = Image.new("RGBA", (width + 10, height + 10), (0, 0, 0, 0))

    mask = Image.new("L", (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=255)

    shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=(1, 8, 18, 220))
    canvas.paste(shadow, (5, 5))

    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = width, height

    if code == "us":
        stripe_h = h / 13.0
        for i in range(13):
            color = (178, 34, 52) if i % 2 == 0 else (245, 247, 250)
            draw.rectangle([0, int(i * stripe_h), w, int((i + 1) * stripe_h)], fill=color)
        draw.rectangle([0, 0, int(w * 0.42), int(h * 7 / 13.0)], fill=(40, 53, 107))
        for r in range(3):
            for c in range(4):
                cx = int(w * 0.06 + c * (w * 0.09))
                cy = int(h * 0.08 + r * (h * 0.16))
                draw.ellipse([cx - 1, cy - 1, cx + 1, cy + 1], fill=(255, 255, 255))
    elif code == "cn":
        draw.rectangle([0, 0, w, h], fill=(222, 41, 16))
        draw.ellipse([int(w * 0.1), int(h * 0.15), int(w * 0.28), int(h * 0.42)], fill=(255, 222, 0))
    elif code == "fr":
        draw.rectangle([0, 0, w // 3, h], fill=(0, 38, 84))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(248, 250, 252))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(237, 41, 57))
    elif code == "ru":
        draw.rectangle([0, 0, w, h // 3], fill=(248, 250, 252))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(0, 57, 166))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(213, 43, 30))
    elif code == "kr":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.22)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(205, 46, 58))
        draw.chord([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], start=0, end=180, fill=(0, 71, 160))
    elif code == "ca":
        draw.rectangle([0, 0, w // 4, h], fill=(216, 6, 33))
        draw.rectangle([w // 4, 0, 3 * w // 4, h], fill=(248, 250, 252))
        draw.rectangle([3 * w // 4, 0, w, h], fill=(216, 6, 33))
        r = int(h * 0.18)
        draw.polygon([(w // 2, h // 2 - r), (w // 2 - r, h // 2 + r // 2), (w // 2 + r, h // 2 + r // 2)], fill=(216, 6, 33))
    elif code == "jp":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.3)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], fill=(188, 0, 45))
    elif code == "de":
        draw.rectangle([0, 0, w, h // 3], fill=(20, 20, 20))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(210, 16, 26))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(255, 206, 0))
    elif code == "ua":
        draw.rectangle([0, 0, w, h // 2], fill=(0, 87, 183))
        draw.rectangle([0, h // 2, w, h], fill=(255, 215, 0))
    elif code == "es":
        draw.rectangle([0, 0, w, h // 4], fill=(170, 21, 27))
        draw.rectangle([0, h // 4, w, 3 * h // 4], fill=(241, 191, 0))
        draw.rectangle([0, 3 * h // 4, w, h], fill=(170, 21, 27))
    elif code == "se":
        draw.rectangle([0, 0, w, h], fill=(0, 106, 167))
        draw.rectangle([int(w * 0.32), 0, int(w * 0.44), h], fill=(254, 204, 2))
        draw.rectangle([0, h // 2 - 4, w, h // 2 + 4], fill=(254, 204, 2))
    elif code == "gb":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w, h)], fill=(255, 255, 255), width=7)
        draw.line([(0, h), (w, 0)], fill=(255, 255, 255), width=7)
        draw.line([(0, 0), (w, h)], fill=(200, 16, 46), width=3)
        draw.line([(0, h), (w, 0)], fill=(200, 16, 46), width=3)
        draw.rectangle([w // 2 - 6, 0, w // 2 + 6, h], fill=(255, 255, 255))
        draw.rectangle([0, h // 2 - 6, w, h // 2 + 6], fill=(255, 255, 255))
        draw.rectangle([w // 2 - 3, 0, w // 2 + 3, h], fill=(200, 16, 46))
        draw.rectangle([0, h // 2 - 3, w, h // 2 + 3], fill=(200, 16, 46))
    elif code == "in":
        draw.rectangle([0, 0, w, h // 3], fill=(255, 153, 51))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(19, 136, 8))
        r = int(h * 0.12)
        draw.ellipse([w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r], outline=(0, 0, 128), width=2)
    elif code == "be":
        draw.rectangle([0, 0, w // 3, h], fill=(20, 20, 20))
        draw.rectangle([w // 3, 0, 2 * w // 3, h], fill=(253, 218, 36))
        draw.rectangle([2 * w // 3, 0, w, h], fill=(239, 51, 64))
    elif code == "ch":
        draw.rectangle([0, 0, w, h], fill=(218, 41, 28))
        draw.rectangle([w // 2 - 5, int(h * 0.18), w // 2 + 5, int(h * 0.82)], fill=(255, 255, 255))
        draw.rectangle([int(w * 0.28), h // 2 - 5, int(w * 0.72), h // 2 + 5], fill=(255, 255, 255))
    elif code == "fi":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        draw.rectangle([int(w * 0.28), 0, int(w * 0.42), h], fill=(0, 47, 108))
        draw.rectangle([0, h // 2 - 5, w, h // 2 + 5], fill=(0, 47, 108))
    elif code == "ae":
        draw.rectangle([0, 0, w, h // 3], fill=(0, 115, 47))
        draw.rectangle([0, h // 3, w, 2 * h // 3], fill=(248, 250, 252))
        draw.rectangle([0, 2 * h // 3, w, h], fill=(15, 15, 15))
        draw.rectangle([0, 0, int(w * 0.26), h], fill=(255, 0, 0))
    elif code == "cz":
        draw.rectangle([0, 0, w, h // 2], fill=(248, 250, 252))
        draw.rectangle([0, h // 2, w, h], fill=(215, 20, 26))
        draw.polygon([(0, 0), (w // 2, h // 2), (0, h)], fill=(17, 69, 126))

    rounded_flag = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    rounded_flag.paste(img, (0, 0), mask=mask)
    rim_draw = ImageDraw.Draw(rounded_flag)
    rim_draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, outline=(0, 245, 212, 185), width=2)
    canvas.paste(rounded_flag, (0, 0), mask=rounded_flag)
    return np.array(canvas)


def make_smooth_capsule_polygon(x0, y0, width, height, rx_left, rx_right, ry, n_arc=24):
    import numpy as np

    ry = min(ry, height * 0.48)
    rx_r = min(rx_right, width * 0.55)
    rx_l = min(rx_left, max(0.0, width - rx_r) * 0.90)

    angles_br = np.linspace(-np.pi / 2, 0, n_arc)
    angles_tr = np.linspace(0, np.pi / 2, n_arc)
    angles_tl = np.linspace(np.pi / 2, np.pi, n_arc)
    angles_bl = np.linspace(np.pi, 3 * np.pi / 2, n_arc)

    x_br = (x0 + width - rx_r) + rx_r * np.cos(angles_br)
    y_br = (y0 + ry) + ry * np.sin(angles_br)

    x_tr = (x0 + width - rx_r) + rx_r * np.cos(angles_tr)
    y_tr = (y0 + height - ry) + ry * np.sin(angles_tr)

    x_tl = (x0 + rx_l) + rx_l * np.cos(angles_tl)
    y_tl = (y0 + height - ry) + ry * np.sin(angles_tl)

    x_bl = (x0 + rx_l) + rx_l * np.cos(angles_bl)
    y_bl = (y0 + ry) + ry * np.sin(angles_bl)

    xs = np.concatenate([x_br, x_tr, x_tl, x_bl])
    ys = np.concatenate([y_br, y_tr, y_tl, y_bl])
    return np.column_stack([xs, ys])


def build_cherenkov_3d_texture(norm_rank, delta_rate, wave_phase, alpha=1.0, h_px=64, w_px=220):
    """
    Creates a translucent-looking 3D Cherenkov radiation capsule texture:
    - Deep indigo/cobalt reactor core base on the left (#1e1b4b -> #1d4ed8)
    - Dazzling Cherenkov aquamarine and neon turquoise on the right (#06b6d4 -> #00f5d4 -> #ccfbf1)
    - Shifts toward reactor-cooldown crimson-amber at the tip if nuclear output is dropping sharply (e.g. Fukushima / German phase-out)
    - Smooth cylindrical 3D glass/plasma shading along Y + travelling quantum Cherenkov pulse along X
    """
    import numpy as np

    y_norm = np.linspace(0.0, 1.0, h_px)[:, None]
    x_norm = np.linspace(0.0, 1.0, w_px)[None, :]

    up_surge = float(np.clip(delta_rate * 8.0, 0.0, 1.0))
    down_drop = float(np.clip(-delta_rate * 8.0, 0.0, 1.0))

    # Left base: deep reactor indigo -> royal cobalt
    r_left = 0.10 + 0.04 * norm_rank
    g_left = 0.16 + 0.22 * norm_rank
    b_left = 0.52 + 0.28 * norm_rank

    # Right tip: dazzling Cherenkov aquamarine & neon turquoise (or warm amber-rose on reactor shutdown)
    r_right_base = 0.05 + 0.28 * norm_rank + 0.35 * up_surge
    g_right_base = 0.82 + 0.16 * norm_rank + 0.08 * up_surge
    b_right_base = 0.88 + 0.12 * norm_rank

    r_right = r_right_base * (1.0 - 0.65 * down_drop) + 0.98 * down_drop
    g_right = g_right_base * (1.0 - 0.55 * down_drop) + 0.42 * down_drop
    b_right = b_right_base * (1.0 - 0.50 * down_drop) + 0.52 * down_drop

    grad_curve = x_norm ** 0.72
    r_base = r_left + (r_right - r_left) * grad_curve
    g_base = g_left + (g_right - g_left) * grad_curve
    b_base = b_left + (b_right - b_left) * grad_curve

    # Travelling Cherenkov quantum ionization wave along X
    wave_pos = wave_phase % 1.0
    cherenkov_pulse = (0.18 + 0.10 * max(up_surge, down_drop)) * np.exp(-((x_norm - wave_pos) ** 2) / (2 * 0.018))

    # Translucent 3D cylindrical glass & core glow profile along Y
    core_glow = 0.52 + 0.52 * np.sin(np.pi * (y_norm ** 0.82))
    glass_specular = 0.42 * np.exp(-((y_norm - 0.75) ** 2) / (2 * 0.0055)) * (0.35 + 0.65 * np.sin(np.pi * x_norm))
    lower_refraction = 0.16 * np.exp(-((y_norm - 0.12) ** 2) / (2 * 0.0050))

    r = np.clip(r_base * core_glow + glass_specular * 0.80 + cherenkov_pulse * 0.70, 0.0, 1.0)
    g = np.clip(g_base * core_glow + glass_specular * 0.98 + cherenkov_pulse * 1.00 + lower_refraction * 0.9, 0.0, 1.0)
    b = np.clip(b_base * core_glow + glass_specular * 1.00 + cherenkov_pulse * 1.00 + lower_refraction * 1.0, 0.0, 1.0)
    a = np.full_like(r, alpha)

    return np.dstack([r, g, b, a])


def get_nuclear_data():
    COUNTRIES_ISO = {
        "United States": "us", "China": "cn", "France": "fr", "Russia / USSR": "ru",
        "South Korea": "kr", "Canada": "ca", "Ukraine": "ua", "Japan": "jp",
        "Germany": "de", "Spain": "es", "Sweden": "se", "United Kingdom": "gb",
        "India": "in", "Belgium": "be", "Switzerland": "ch", "Finland": "fi",
        "UAE": "ae", "Czechia": "cz"
    }

    # Annual Nuclear Electricity Generation in Terawatt-hours (TWh) — IAEA PRIS & World Nuclear Association (1965 - Oct 2026)
    ANCHORS = {
        "United States":  {1965: 3.8,  1970: 21.8, 1975: 172.5, 1980: 251.1, 1985: 383.7, 1990: 576.9, 2000: 753.9, 2010: 807.0, 2020: 789.9, 2026: 782.0},
        "France":         {1965: 0.9,  1970: 5.7,  1975: 18.3,  1980: 61.3,  1985: 224.1, 1990: 314.1, 2000: 415.2, 2005: 451.5, 2015: 437.4, 2022: 294.7, 2026: 365.0},
        "China":          {1965: 0.0,  1990: 0.0,  1995: 12.8,  2000: 16.7,  2005: 53.1,  2010: 73.9,  2015: 170.8, 2020: 366.2, 2026: 455.0},
        "Russia / USSR":  {1965: 1.4,  1970: 3.7,  1975: 20.2,  1980: 72.9,  1985: 167.0, 1990: 118.3, 2000: 130.7, 2010: 170.4, 2020: 215.7, 2026: 224.0},
        "South Korea":    {1965: 0.0,  1975: 0.0,  1980: 3.5,   1985: 16.7,  1990: 52.9,  2000: 109.0, 2010: 148.6, 2015: 164.8, 2020: 160.2, 2026: 188.0},
        "Canada":         {1965: 0.1,  1970: 1.0,  1975: 12.6,  1980: 38.0,  1985: 60.5,  1990: 73.0,  2000: 72.8,  2010: 90.7,  2020: 97.5,  2026: 92.0},
        "Japan":          {1965: 0.03, 1970: 4.6,  1975: 25.1,  1980: 82.6,  1985: 159.6, 1990: 202.3, 2000: 322.0, 2005: 304.8, 2010: 288.2, 2012: 15.9, 2014: 0.0, 2020: 38.8, 2026: 86.0},
        "Germany":        {1965: 0.1,  1970: 6.5,  1975: 24.1,  1980: 55.6,  1985: 138.6, 1990: 152.5, 2000: 169.6, 2005: 163.1, 2010: 140.6, 2015: 91.8,  2020: 64.4, 2022: 34.7, 2023: 0.0, 2026: 0.0},
        "Ukraine":        {1965: 0.0,  1975: 0.0,  1980: 14.2,  1985: 53.3,  1990: 76.2,  2000: 77.3,  2005: 88.8,  2010: 89.2,  2020: 76.2,  2026: 53.0},
        "Spain":          {1965: 0.0,  1970: 0.9,  1975: 7.5,   1980: 5.2,   1985: 28.0,  1990: 54.3,  2000: 62.2,  2005: 57.5,  2010: 61.9,  2020: 58.3,  2026: 56.5},
        "Sweden":         {1965: 0.02, 1970: 0.06, 1975: 12.0,  1980: 26.5,  1985: 58.6,  1990: 68.2,  2000: 57.3,  2005: 72.4,  2010: 57.8,  2020: 49.2,  2026: 51.0},
        "United Kingdom": {1965: 15.1, 1970: 26.0, 1975: 30.3,  1980: 37.0,  1985: 61.1,  1990: 65.7,  2000: 85.1,  2005: 81.6,  2010: 62.1,  2020: 50.3,  2026: 41.5},
        "India":          {1965: 0.0,  1970: 2.4,  1975: 2.6,   1980: 3.0,   1985: 4.7,   1990: 6.1,   2000: 15.8,  2005: 17.8,  2010: 23.1,  2020: 44.6,  2026: 54.5},
        "Belgium":        {1965: 0.0,  1970: 0.05, 1975: 6.8,   1980: 12.5,  1985: 34.6,  1990: 42.7,  2000: 48.2,  2005: 47.6,  2010: 47.9,  2020: 34.4,  2026: 31.0},
        "Switzerland":    {1965: 0.0,  1970: 1.8,  1975: 7.7,   1980: 14.3,  1985: 22.6,  1990: 23.6,  2000: 26.4,  2005: 23.3,  2010: 26.5,  2020: 23.0,  2026: 23.5},
        "Finland":        {1965: 0.0,  1975: 0.0,  1980: 7.0,   1985: 19.1,  1990: 19.2,  2000: 22.5,  2005: 23.3,  2010: 22.8,  2020: 23.3,  2026: 34.5},
        "UAE":            {1965: 0.0,  2019: 0.0,  2020: 1.6,   2022: 20.1,  2024: 32.0,  2026: 40.5},
        "Czechia":        {1965: 0.0,  1980: 0.0,  1985: 2.4,   1990: 12.6,  2000: 13.6,  2005: 24.7,  2010: 28.0,  2020: 30.0,  2026: 30.8}
    }
    return COUNTRIES_ISO, ANCHORS


def run_worker():
    import math
    import wave
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import matplotlib.animation as animation
    from matplotlib.patches import Polygon, FancyBboxPatch
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    import imageio_ffmpeg

    FPS = 30
    DURATION_SEC = 40
    TOTAL_FRAMES = FPS * DURATION_SEC

    COUNTRIES_ISO, ANCHORS = get_nuclear_data()

    START_YEAR = 1965.0
    END_YEAR = 2026.83
    TITLE_MAIN = "NUCLEAR POWER RACE: ATOMIC ENERGY"
    TITLE_SUB = "ANNUAL NUCLEAR ELECTRICITY GENERATION IN TWh (1965 - OCT 2026)"
    FINAL_OUTPUT = "global_nuclear_power_1965_2026_shorts.mp4"

    print(" -> Generating rounded Cherenkov 3D flags for all countries...")
    flags = {country: create_cherenkov_flag(code, 80, 52, 10) for country, code in COUNTRIES_ISO.items()}

    print(" -> Synthesizing royalty-free soundtrack (Cherenkov Quantum Resonance - CC0 License)...")
    audio_path = os.path.join(TEMP_DIR, "cherenkov_quantum.wav")
    license_lines = [
        "MUSIC LICENSE CERTIFICATE (CC0 1.0 Universal - Public Domain Dedication)",
        "=======================================================================",
        "Track Title: Cherenkov Quantum Resonance (Atmospheric Sci-Fi Reactor Drone & Crystalline Pulse Score)",
        "License: Creative Commons Zero (CC0 1.0 Universal)",
        "Status: 100% Royalty-Free / Safe for YouTube Shorts, Instagram Reels, TikTok monetization.",
        "Permissions: Commercial and non-commercial use, modification, and distribution permitted without attribution."
    ]
    with open("MUSIC_LICENSE_CC0.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(license_lines) + "\n")

    sample_rate = 44100
    n_samples = sample_rate * DURATION_SEC
    t = np.linspace(0, DURATION_SEC, n_samples, endpoint=False)

    # Atmospheric sci-fi reactor progression: F# minor -> D major -> B minor -> C#7
    freqs_base = np.select(
        [(t % 10) < 2.5, (t % 10) < 5.0, (t % 10) < 7.5, (t % 10) >= 7.5],
        [92.50, 73.42, 61.74, 69.30]
    )

    # Deep reactor core magnetic hum (sub-bass + slow LFO modulation)
    core_hum = (
        0.24 * np.sin(2 * math.pi * freqs_base * t)
        + 0.10 * np.sin(2 * math.pi * (freqs_base * 0.5) * t)
    ) * (0.70 + 0.30 * np.sin(2 * math.pi * 1.5 * t))

    # Shimmering Cherenkov glass pad (stereo detuned)
    pad_l = 0.14 * np.sin(2 * math.pi * (freqs_base * 2.0) * t + 0.4 * np.sin(2 * math.pi * 0.5 * t))
    pad_r = 0.14 * np.sin(2 * math.pi * (freqs_base * 3.0) * t + 0.8)

    # Crystalline quantum / Geiger harmonic arpeggio (6 pulses per second)
    q_phase = (t * 6.0) % 1.0
    q_env = np.exp(-9.0 * q_phase) * (1.0 - np.exp(-120.0 * q_phase))
    q_mult = np.select(
        [((t * 6.0).astype(int) % 4) == 0, ((t * 6.0).astype(int) % 4) == 1,
         ((t * 6.0).astype(int) % 4) == 2, ((t * 6.0).astype(int) % 4) == 3],
        [3.0, 4.0, 6.0, 4.0]
    )
    quantum_arp = 0.09 * np.sin(2 * math.pi * (freqs_base * q_mult) * t) * q_env

    envelope = np.ones_like(t)
    fade_len = sample_rate * 2
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    stereo_left = np.clip((core_hum + pad_l + quantum_arp) * envelope, -0.95, 0.95)
    stereo_right = np.clip((core_hum + pad_r + quantum_arp * 0.90) * envelope, -0.95, 0.95)

    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = (stereo_left * 32767).astype(np.int16)
    interleaved[1::2] = (stereo_right * 32767).astype(np.int16)

    with wave.open(audio_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())

    print(" -> Building 1965-2026 nuclear generation matrix with smooth Hann-window rank transitions...")
    fine_years = np.linspace(START_YEAR, END_YEAR, TOTAL_FRAMES)
    val_dict = {}
    for country, anchors in ANCHORS.items():
        yrs = sorted(list(anchors.keys()))
        vals = [anchors[y] for y in yrs]
        val_dict[country] = np.interp(fine_years, yrs, vals)

    df_values = pd.DataFrame(val_dict, index=fine_years)
    # Countries with <= 0.05 TWh (e.g. Germany after April 2023 shutdown) exit the active ranking smoothly
    df_values = df_values.where(df_values > 0.05, np.nan)

    df_deltas = df_values.pct_change(periods=15).fillna(0.0)
    df_deltas_smooth = df_deltas.rolling(window=20, min_periods=1, center=True).mean().fillna(0.0)

    df_ranks = df_values.rank(axis=1, method='first', ascending=True).fillna(0.0)
    win_size = 35
    hann_win = np.hanning(win_size)
    hann_win /= hann_win.sum()
    df_ranks_smooth = df_ranks.apply(
        lambda col: np.convolve(np.pad(col.values, (win_size // 2, win_size // 2), mode='edge'), hann_win, mode='valid')[:len(col)]
    )

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_exe

    print(f" -> Rendering 40-second Cherenkov 3D HD 9:16 video ({TOTAL_FRAMES} frames at {FPS} FPS)...")
    BG_OUTER = '#030914'
    BG_PLOT = '#061224'

    fig = plt.figure(figsize=(9, 16), dpi=120)
    fig.patch.set_facecolor(BG_OUTER)

    # Pulsing Cherenkov quantum particles in reactor pool background
    q_ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    q_ax.set_xlim(0, 1)
    q_ax.set_ylim(0, 1)
    q_ax.set_xticks([])
    q_ax.set_yticks([])

    np.random.seed(137)
    n_quanta = 85
    base_px = np.random.uniform(0.03, 0.97, n_quanta)
    base_py = np.random.uniform(0.03, 0.97, n_quanta)
    base_ps = np.random.uniform(5, 36, n_quanta)
    base_pa = np.random.uniform(0.08, 0.42, n_quanta)
    q_colors = ['#00f5d4' if i % 2 == 0 else '#38bdf8' for i in range(n_quanta)]
    q_scatter = q_ax.scatter(base_px, base_py, s=base_ps, c=q_colors, alpha=0.25, edgecolors='none')

    # Smooth Rounded Reactor Pool Header Capsule
    header_box = FancyBboxPatch(
        (0.04, 0.882), 0.92, 0.092,
        boxstyle="round,pad=0.01,rounding_size=0.035",
        transform=fig.transFigure,
        facecolor='#081a33', edgecolor='#00f5d4', linewidth=1.8, alpha=0.96, zorder=2
    )
    fig.patches.append(header_box)

    fig.text(
        0.5, 0.946, TITLE_MAIN,
        color='#f0fdfa', fontsize=19.8, fontweight='bold', fontfamily='DejaVu Sans', ha='center', va='center', zorder=4
    )
    fig.text(
        0.5, 0.916, TITLE_SUB,
        color='#2dd4bf', fontsize=9.4, fontweight='bold', fontfamily='DejaVu Sans Mono', ha='center', va='center', zorder=4
    )

    prog_bg = FancyBboxPatch(
        (0.10, 0.893), 0.80, 0.006,
        boxstyle="round,pad=0,rounding_size=0.003",
        transform=fig.transFigure,
        facecolor='#0f2942', edgecolor='none', alpha=0.9, zorder=3
    )
    prog_fg = FancyBboxPatch(
        (0.10, 0.893), 0.01, 0.006,
        boxstyle="round,pad=0,rounding_size=0.003",
        transform=fig.transFigure,
        facecolor='#00f5d4', edgecolor='none', alpha=0.95, zorder=4
    )
    fig.patches.extend([prog_bg, prog_fg])

    ax = fig.add_axes([0.38, 0.06, 0.58, 0.79])

    top_n = 12
    max_rank = len(COUNTRIES_ISO)
    min_visible_rank = max_rank - top_n + 1.0

    ax_w_in = 0.58 * 9.0
    ax_h_in = 0.79 * 16.0
    bar_h = 0.56
    ry = bar_h * 0.46

    def update(frame_idx):
        ax.clear()
        ax.set_facecolor(BG_PLOT)

        progress = (frame_idx + 1) / float(TOTAL_FRAMES)
        prog_fg.set_width(max(0.01, 0.80 * progress))

        # Smooth orbital / rising quantum particle motion + Cherenkov glow pulsation
        cur_py = (base_py + frame_idx * 0.00075) % 1.0
        cur_px = (base_px + 0.010 * np.sin(frame_idx * 0.05 + np.arange(n_quanta))) % 1.0
        q_scatter.set_offsets(np.column_stack([cur_px, cur_py]))
        cur_sizes = base_ps * (0.80 + 0.35 * np.sin(frame_idx * 0.12 + np.arange(n_quanta)))
        q_scatter.set_sizes(cur_sizes)
        twinkle = base_pa * (0.60 + 0.40 * np.sin(frame_idx * 0.14 + np.arange(n_quanta)))
        q_scatter.set_alpha(twinkle)

        current_time = df_values.index[frame_idx]
        year_int = int(current_time)
        month_int = min(12, max(1, int((current_time - year_int) * 12) + 1))
        month_names = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        date_str = f"{month_names[month_int - 1]} {year_int}"

        vals_row = df_values.iloc[frame_idx]
        ranks_row = df_ranks_smooth.iloc[frame_idx]
        deltas_row = df_deltas_smooth.iloc[frame_idx]

        visible = ranks_row[ranks_row >= min_visible_rank - 0.7].dropna()
        max_val = max(vals_row.max(), 10.0)

        x_max = max_val * 1.35
        y_min, y_max = min_visible_rank - 0.65, max_rank + 0.65
        ax.set_xlim(0, x_max)
        ax.set_ylim(y_min, y_max)

        ax.xaxis.grid(True, color='#0f2942', linestyle='--', linewidth=1.0, alpha=0.75, zorder=0)
        ax.set_axisbelow(True)

        rx_right = ry * (x_max / (y_max - y_min)) * (ax_h_in / ax_w_in) * 0.68
        rx_left = rx_right * 0.22
        wave_global = (frame_idx * 0.026) % 1.0

        for country, smooth_y in visible.items():
            val = vals_row[country]
            if pd.isna(val) or val <= 0.05:
                continue

            alpha = 1.0
            if smooth_y < min_visible_rank:
                alpha = max(0.0, min(1.0, (smooth_y - (min_visible_rank - 0.7)) / 0.7))

            norm_rank = np.clip((smooth_y - min_visible_rank) / max(1, top_n - 1), 0, 1)
            rank_num = max(1, min(top_n, int(round(max_rank - smooth_y + 1))))
            y0 = smooth_y - bar_h / 2.0
            d_rate = float(deltas_row[country])

            vis_val = max(val, max_val * 0.058)

            # 1. Outer Cherenkov Halo / Deep Pool Shadow
            shadow_verts = make_smooth_capsule_polygon(
                max_val * 0.008, y0 - 0.085, vis_val, bar_h, rx_left, rx_right, ry, n_arc=20
            )
            shadow_poly = Polygon(
                shadow_verts, closed=True, facecolor='#01060d', alpha=0.85 * alpha, edgecolor='none', zorder=2
            )
            ax.add_patch(shadow_poly)

            # 2. 3D Lower Translucent Extrusion Bevel
            base_color = '#0d9488' if d_rate > 0.025 else ('#881337' if d_rate < -0.02 else '#1e3a8a')
            base_verts = make_smooth_capsule_polygon(
                max_val * 0.004, y0 - 0.042, vis_val, bar_h, rx_left, rx_right, ry, n_arc=20
            )
            base_poly = Polygon(
                base_verts, closed=True, facecolor=base_color, alpha=0.90 * alpha, edgecolor='none', zorder=2.5
            )
            ax.add_patch(base_poly)

            # 3. Main Smooth Translucent 3D Capsule with Cherenkov Radiation Gradient
            bar_verts = make_smooth_capsule_polygon(0, y0, vis_val, bar_h, rx_left, rx_right, ry, n_arc=24)
            clip_poly = Polygon(bar_verts, closed=True, facecolor='none', edgecolor='none', zorder=3)
            ax.add_patch(clip_poly)

            tex = build_cherenkov_3d_texture(
                norm_rank, d_rate, wave_phase=wave_global - norm_rank * 0.35, alpha=alpha
            )
            im = ax.imshow(
                tex, extent=[0, vis_val, y0, y0 + bar_h],
                aspect='auto', origin='lower', interpolation='bicubic', zorder=3.5
            )
            im.set_clip_path(clip_poly)

            # 4. Luminous Cherenkov Turquoise Rim Outline
            rim_color = '#99f6e4' if d_rate > 0.025 else ('#fda4af' if d_rate < -0.02 else '#2dd4bf')
            rim_poly = Polygon(
                bar_verts, closed=True, facecolor='none',
                edgecolor=rim_color, linewidth=1.2, alpha=0.82 * alpha, zorder=4.5
            )
            ax.add_patch(rim_poly)

            # 5. Rank Badge
            rank_color = '#00f5d4' if rank_num <= 3 else '#64748b'
            ax.text(
                -0.62, smooth_y, f"#{rank_num:02d}",
                transform=ax.get_yaxis_transform(),
                color=rank_color, fontsize=10.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6, clip_on=False
            )

            # 6. Country Name
            ax.text(
                -0.165, smooth_y, country,
                transform=ax.get_yaxis_transform(),
                color='#f0fdfa', fontsize=12.0, fontweight='bold', fontfamily='DejaVu Sans',
                va='center', ha='right', alpha=alpha, zorder=6, clip_on=False
            )

            # 7. Rounded Cherenkov Flag
            if country in flags:
                imagebox = OffsetImage(flags[country], zoom=0.44, alpha=alpha)
                ab = AnnotationBbox(
                    imagebox, (-0.078, smooth_y),
                    xycoords=('axes fraction', 'data'),
                    frameon=False,
                    box_alignment=(0.5, 0.5),
                    zorder=5,
                    annotation_clip=False
                )
                ax.add_artist(ab)

            # 8. Value Label in TWh + Reactor Surge/Shutdown Indicator
            if d_rate > 0.025:
                tag = " ▲"
                lbl_col = '#99f6e4'
            elif d_rate < -0.02:
                tag = " ▼"
                lbl_col = '#fda4af'
            else:
                tag = ""
                lbl_col = '#5eead4'

            ax.text(
                vis_val + max_val * 0.022, smooth_y, f"{val:,.1f} TWh{tag}",
                color=lbl_col, fontsize=11.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6
            )

        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#00f5d4')
        ax.spines['left'].set_linewidth(1.6)
        ax.spines['bottom'].set_color('#1e3a8a')
        ax.tick_params(axis='x', colors='#94a3b8', labelsize=9.5)
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x)}"))

        # Smooth Rounded Reactor Telemetry HUD Box in bottom-right corner
        hud_box = FancyBboxPatch(
            (0.46, 0.025), 0.50, 0.15,
            boxstyle="round,pad=0.015,rounding_size=0.04",
            transform=ax.transAxes,
            facecolor='#081a33', edgecolor='#00f5d4', linewidth=1.6, alpha=0.95, zorder=5
        )
        ax.add_patch(hud_box)

        ax.text(
            0.93, 0.125, f"{year_int}", transform=ax.transAxes,
            color='#f0fdfa', fontsize=38, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )
        ax.text(
            0.93, 0.075, f"{date_str}", transform=ax.transAxes,
            color='#00f5d4', fontsize=13.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )
        total_twh = float(vals_row.dropna().sum())
        ax.text(
            0.93, 0.043, f"WORLD NUCLEAR: {total_twh:,.0f} TWh", transform=ax.transAxes,
            color='#5eead4', fontsize=8.8, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )

        if frame_idx % 120 == 0 or frame_idx == TOTAL_FRAMES - 1:
            pct = int((frame_idx + 1) / TOTAL_FRAMES * 100)
            print(f"    Rendering progress: {pct}% ({frame_idx + 1}/{TOTAL_FRAMES} frames)")

    temp_video = os.path.join(TEMP_DIR, "silent_nuclear_video.mp4")
    writer = animation.FFMpegWriter(fps=FPS, codec='libx264', bitrate=5500, extra_args=['-pix_fmt', 'yuv420p'])
    anim = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000 / FPS, repeat=False)
    anim.save(temp_video, writer=writer)
    plt.close(fig)

    print(" -> Mixing audio track and encoding final MP4...")
    subprocess.check_call([
        ffmpeg_exe, "-y",
        "-i", temp_video,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        FINAL_OUTPUT
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" -> SUCCESS! Final video saved as: {FINAL_OUTPUT}")


if __name__ == "__main__":
    if "--worker" in sys.argv:
        run_worker()
    else:
        run_bootstrap()
