"""Erzeugt das Basketball-Icon (icon.svg + PNGs fuer iPhone/Android-Homebildschirm)."""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent
BG, BALL, SEAM = (255, 244, 232), (232, 102, 28), (38, 20, 10)
# Bogen-Naht: Kreis mit Mittelpunkt (cx -/+ DX, cy), Radius RR (in Einheiten von R)
DX, RR = 1.30, 0.98


def render(size, full_bleed=True):
    s = 4
    n = size * s
    img = Image.new("RGB", (n, n), BG)
    R = n * 0.40
    c = n / 2
    lw = max(2, int(R * 0.075))
    ball = Image.new("RGB", (n, n), BALL)
    d = ImageDraw.Draw(ball)
    d.line([(c, 0), (c, n)], fill=SEAM, width=lw)
    d.line([(0, c), (n, c)], fill=SEAM, width=lw)
    for sign in (-1, 1):
        cx = c + sign * DX * R
        r = RR * R
        d.ellipse([cx - r, c - r, cx + r, c + r], outline=SEAM, width=lw)
    mask = Image.new("L", (n, n), 0)
    ImageDraw.Draw(mask).ellipse([c - R, c - R, c + R, c + R], fill=255)
    img.paste(ball, (0, 0), mask)
    ImageDraw.Draw(img).ellipse([c - R, c - R, c + R, c + R], outline=SEAM, width=lw)
    return img.resize((size, size), Image.LANCZOS)


for name, size in (("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)):
    render(size).save(OUT / name, optimize=True)

# SVG-Variante fuer Browser-Tab und Seitenkopf (gleiche Geometrie, Viewbox 100)
R = 40
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="#fff4e8"/>
<defs><clipPath id="b"><circle cx="50" cy="50" r="{R}"/></clipPath></defs>
<circle cx="50" cy="50" r="{R}" fill="#e8661c"/>
<g clip-path="url(#b)" fill="none" stroke="#26140a" stroke-width="3">
<path d="M50 0V100M0 50H100"/>
<circle cx="{50 - DX * R}" cy="50" r="{RR * R}"/><circle cx="{50 + DX * R}" cy="50" r="{RR * R}"/></g>
<circle cx="50" cy="50" r="{R}" fill="none" stroke="#26140a" stroke-width="3"/></svg>
"""
(OUT / "icon.svg").write_text(svg)
