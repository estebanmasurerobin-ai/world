"""Version sombre du logo : fond et W inversés (blanc <-> noir), l'étoile garde ses couleurs.
Usage : python3 sombre.py source.png sortie.png"""
import sys
from PIL import Image
import colorsys
im = Image.open(sys.argv[1]).convert('RGB'); px = im.load(); W, H = im.size
# Zone de l'étoile : les pixels nettement colorés, avec une petite marge
pts = [(x, y) for y in range(H) for x in range(W)
       if max(px[x, y]) - min(px[x, y]) > 51 and colorsys.rgb_to_hls(*[c / 255 for c in px[x, y]])[2] > .3]
x0, y0 = min(p[0] for p in pts) - 4, min(p[1] for p in pts) - 4
x1, y1 = max(p[0] for p in pts) + 4, max(p[1] for p in pts) + 4
out = Image.new('RGB', im.size); po = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        if x0 <= x <= x1 and y0 <= y <= y1:
            m = min(r, g, b); po[x, y] = (r - m, g - m, b - m)  # couleur posée sur noir au lieu de blanc
        else:
            po[x, y] = (255 - r, 255 - g, 255 - b)
out.save(sys.argv[2])
