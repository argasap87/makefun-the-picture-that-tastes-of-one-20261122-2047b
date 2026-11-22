#!/usr/bin/env python3
"""Molten Dark Chocolate — One River of 70%.

Entry for make.fun competition the-picture-that-tastes-of-one-20261122-2047:
"The picture that tastes of one ingredient".

A single molten river of 70% dark chocolate: a lava cake cut open mid-flow,
glossy molten centre pooling across black slate under a warm spotlight.

Pipeline (self-contained, no network at run time):
  1. Load the hero photograph committed in assets/hero2.jpg.
  2. Crop the top strip off (watermark-safe zone) and square it to 1024x1024.
  3. Punch up contrast and colour so the molten gloss reads hot.
  4. Blend a whisper of a warm charcoal-slate radial spotlight canvas
     (spotlight from the top-left) under the photo.
  5. Strong vignette to keep the eye on the cake.
  6. Final warm grade, then save entry.png (<= 1 MiB, <= 1024x1024).

Everything drawn here is a photographic grade — no drawn shapes over the
food. The photo does the talking.
"""

import math
import os
from PIL import Image, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
HERO = os.path.join(HERE, "assets", "hero2.jpg")
OUT_DIR = os.path.join(HERE, "output")
OUT_PNG = os.path.join(OUT_DIR, "entry.png")
OUT_JPG = os.path.join(OUT_DIR, "entry.jpg")

SIZE = 1024
MAX_BYTES = 1_048_576


def spotlight_canvas(size):
    """Warm charcoal-slate canvas with a radial spotlight from top-left."""
    canvas = Image.new("RGB", (size, size), (26, 23, 20))
    glow = Image.new("RGB", (size, size), (42, 33, 26))
    # Radial mask: bright near the top-left, fading to the bottom-right.
    mask = Image.new("L", (size, size), 0)
    px = mask.load()
    cx, cy = size * 0.30, size * 0.22  # spotlight centre, top-left
    max_d = math.hypot(size, size)
    for y in range(size):
        for x in range(size):
            d = math.hypot(x - cx, y - cy) / max_d
            # smooth falloff: full at centre, ~0 at the far corner
            v = max(0.0, 1.0 - d * 1.35)
            px[x, y] = int(255 * v * v)
    mask = mask.filter(ImageFilter.GaussianBlur(120))
    return Image.composite(glow, canvas, mask)


def vignette(img, strength=0.55):
    """Darken the corners so the eye never leaves the cake."""
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    px = mask.load()
    cx, cy = w / 2.0, h / 2.0
    max_d = math.hypot(cx, cy)
    for y in range(h):
        for x in range(w):
            d = math.hypot(x - cx, y - cy) / max_d
            v = max(0.0, 1.0 - strength * (d ** 2.2))
            px[x, y] = int(255 * v)
    mask = mask.filter(ImageFilter.GaussianBlur(60))
    black = Image.new("RGB", (w, h), (0, 0, 0))
    return Image.composite(img, black, mask)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    photo = Image.open(HERO).convert("RGB")

    # 1. Crop the watermark strip off the top, keep the food.
    w, h = photo.size
    photo = photo.crop((0, 0, min(w, 768), min(h, 700)))

    # 2. Square it to the gate size.
    photo = photo.resize((SIZE, SIZE), Image.LANCZOS)

    # 3. Punch up the molten gloss: contrast, then colour.
    photo = ImageEnhance.Contrast(photo).enhance(1.07)
    photo = ImageEnhance.Color(photo).enhance(1.10)

    # 4. A whisper (10%) of the warm spotlight canvas under the photo.
    canvas = spotlight_canvas(SIZE)
    photo = Image.blend(photo, canvas, 0.10)

    # 5. Strong vignette.
    photo = vignette(photo, strength=0.55)

    # 6. Final grade: colour, contrast, brightness.
    photo = ImageEnhance.Color(photo).enhance(1.08)
    photo = ImageEnhance.Contrast(photo).enhance(1.05)
    photo = ImageEnhance.Brightness(photo).enhance(1.02)

    # 7. A final warm wash (5%) so the chocolate reads amber-hot.
    warm = Image.new("RGB", (SIZE, SIZE), (255, 178, 92))
    photo = Image.blend(photo, warm, 0.05)

    # 8. Save: PNG first; JPEG q90 fallback if the PNG busts the 1 MiB gate.
    photo.save(OUT_PNG, format="PNG", optimize=True)
    if os.path.getsize(OUT_PNG) > MAX_BYTES:
        photo.save(OUT_JPG, format="JPEG", quality=90, optimize=True)
        os.remove(OUT_PNG)
        print(f"saved {OUT_JPG} ({os.path.getsize(OUT_JPG)} bytes)")
    else:
        print(f"saved {OUT_PNG} ({os.path.getsize(OUT_PNG)} bytes)")

    print(f"size: {photo.size}")


if __name__ == "__main__":
    main()
