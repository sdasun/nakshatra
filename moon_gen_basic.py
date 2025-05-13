from PIL import Image, ImageDraw, ImageChops
import os
import math

# Configuration
SIZE       = 512            # px
OUTPUT_DIR = "moon_phases"
PHASES     = 30
R          = SIZE // 2
CENTER     = (R, R)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def make_phase_image(i: int) -> Image.Image:
    """
    i=0             → New Moon (all dark/transparent)
    i=PHASES//2     → Full Moon (all light)
    i=PHASES-1      → New Moon (all dark)
    0→mid: waxing  (light on right)
    mid→end: waning (light on left)
    """
    mid = PHASES // 2

    # 1) start with a full white circle
    img = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, SIZE, SIZE], fill=(255,255,255,255))

    # special-case full moon: skip masking altogether
    if i == mid:
        return img

    # build the shadow mask
    mask = Image.new("L", (SIZE, SIZE), 0)
    md   = ImageDraw.Draw(mask)

    if i <= mid:
        frac   = i / mid            # 0→1
        offset = -2 * R * frac      # shift shadow left
    else:
        frac   = 1 - (i - mid) / mid  # 1→0
        offset =  2 * R * frac        # shift shadow right

    md.ellipse([
        CENTER[0] - R + offset,
        CENTER[1] - R,
        CENTER[0] + R + offset,
        CENTER[1] + R
    ], fill=255)

    # subtract the mask from alpha
    alpha     = img.split()[-1]
    new_alpha = ImageChops.subtract(alpha, mask)
    img.putalpha(new_alpha)

    return img

if __name__ == "__main__":
    for idx in range(PHASES):
        img = make_phase_image(idx)
        img.save(f"{OUTPUT_DIR}/moon_phase_{idx:02d}.png")
    print(f"✅ Generated {PHASES} transparent moon phases in ./{OUTPUT_DIR}/")
