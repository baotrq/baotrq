"""Turn a photo into card/ascii.txt. Run locally once: python card/ascii.py photo.png

Needs Pillow. Works best on a cut-out PNG (transparent background): transparent pixels become
spaces, and every pixel of the subject gets a glyph, so dark hair and clothes keep their shape.
Tune --contrast / --gamma until the face reads well, then commit ascii.txt.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

RAMP = ".'`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"  # light to dense

p = argparse.ArgumentParser()
p.add_argument("photo")
p.add_argument("--cols", type=int, default=38)  # card/build.py ART_COLS
p.add_argument("--rows", type=int, default=25)
p.add_argument("--contrast", type=float, default=1.4)
p.add_argument("--gamma", type=float, default=1.0, help="<1 brightens the shadows")
p.add_argument("--center", type=float, nargs=2, default=(0.5, 0.4), metavar=("X", "Y"))
p.add_argument("--ramp", default=RAMP, help="glyphs from light to dense")
a = p.parse_args()
RAMP = a.ramp

src = ImageOps.exif_transpose(Image.open(a.photo)).convert("RGBA")
size = (a.cols, a.rows * 2)  # a character is about twice as tall as it is wide
lum = ImageOps.fit(src.convert("L"), size, Image.LANCZOS, centering=a.center)
alpha = ImageOps.fit(src.getchannel("A"), size, Image.LANCZOS, centering=a.center)
lum = ImageEnhance.Contrast(ImageOps.autocontrast(lum, cutoff=2, mask=alpha.point(lambda v: 255 * (v > 128)))).enhance(a.contrast)
lum, alpha = lum.resize((a.cols, a.rows), Image.LANCZOS), alpha.resize((a.cols, a.rows), Image.LANCZOS)

L, A = lum.load(), alpha.load()
lines = []
for y in range(a.rows):
    row = ""
    for x in range(a.cols):
        if A[x, y] < 100:
            row += " "
        else:
            v = (L[x, y] / 255) ** a.gamma
            row += RAMP[min(int(v * len(RAMP)), len(RAMP) - 1)]
    lines.append(row.rstrip())
(Path(__file__).parent / "ascii.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
