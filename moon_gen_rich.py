from PIL import Image, ImageDraw, ImageChops, ImageFilter
import os
import math

# ————— CONFIG —————
SIZE         = 512               # output size in px
PHASES       = 30                # number of frames
OUTPUT_DIR   = "images/moon_phases"
MOON_TEXTURE = "images/moon.png"        # path to your real moon texture
BLUR_RADIUS  = 20                # softness of the terminator edge
# ——————————————————

R      = SIZE // 2
CENTER = (R, R)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# preload & resize texture
base_tex = Image.open(MOON_TEXTURE).convert("RGBA")
base_tex = base_tex.resize((SIZE, SIZE), Image.LANCZOS)

def make_phase_image(i: int) -> Image.Image:
    mid = PHASES // 2

    # 1) start with the textured moon
    img = base_tex.copy()

    # full-moon special case
    if i == mid:
        # just return the full lit texture (alpha=255)
        img.putalpha(255)
        return img

    # 2) build a shadow mask
    mask = Image.new("L", (SIZE, SIZE), 0)
    md   = ImageDraw.Draw(mask)

    if i <= mid:
        frac   = i / mid              # 0→1
        offset = -2 * R * frac        # shift mask circle left
    else:
        frac   = 1 - (i - mid) / mid  # 1→0
        offset =  2 * R * frac        # shift mask circle right

    # draw the hard‐edge mask
    md.ellipse([
        CENTER[0] - R + offset,
        CENTER[1] - R,
        CENTER[0] + R + offset,
        CENTER[1] + R
    ], fill=255)

    # 3) blur the mask to soften the terminator
    mask = mask.filter(ImageFilter.GaussianBlur(radius=BLUR_RADIUS))

    # 4) apply mask: subtract shadow-area from alpha
    alpha = Image.new("L", (SIZE, SIZE), 255)
    new_alpha = ImageChops.subtract(alpha, mask)
    img.putalpha(new_alpha)

    return img

if __name__ == "__main__":
    for idx in range(PHASES):
        out = make_phase_image(idx)
        out.save(os.path.join(OUTPUT_DIR, f"phase_{idx:02d}.png"))
    print(f"✅ Generated {PHASES} realistic moon phases in ./{OUTPUT_DIR}/")
