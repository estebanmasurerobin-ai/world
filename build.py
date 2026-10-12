"""Construit World dans docs/ (dossier publié par GitHub Pages).

World est une application à part, tirée de l'éditeur de Plume (plume.html, publiée sur claude.ai
avec Claude, et qui reste inchangée). World n'a AUCUNE intelligence artificielle : ce script ajoute
l'en-tête d'application (icône, manifeste, plein écran iOS), renomme Plume en World, masque tout
ce qui touche à l'IA et remplace la partie « IA » du texte d'exemple.

Usage : python3 build.py
"""
import hashlib, pathlib, re, shutil

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / 'world'
OUT = ROOT / 'docs'
EDITOR = ROOT / 'plume.html'

HEAD = '''<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="World">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" sizes="180x180" href="icone-noire-180.png">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="icon" type="image/png" href="icone-noire-192.png">
<script src="standalone.js"></script>
<style>
/* Version sans IA : aucun bouton, menu ou panneau d'IA */
html.no-ai #ai-btn, html.no-ai .selbar .needs-ai, html.no-ai #cpanel, html.no-ai #ai-dock, html.no-ai #ai-side{display:none!important}
</style>
'''

# Texte d'exemple : la section sur l'IA devient une section sur la concentration seule.
SAMPLE_AI = re.compile(r'<h2>Concentration et IA</h2>.*?(<p>Pour élargir la colonne)', re.S)
SAMPLE_NO_AI = ("<h2>Concentration</h2>\n<p>Le mode concentration grise tout le texte sauf le paragraphe où se trouve votre curseur. "
                "Le bouton à trois lignes, en haut à droite, l'active ou le désactive. La ligne où vous écrivez reste toujours au milieu de l'écran.</p>\n"
                "<p>Sélectionnez un passage pour le copier ou le rechercher sur le web.</p>\n\\1")

html = EDITOR.read_text(encoding='utf-8')
# Le fichier publié sur claude.ai contient déjà <head> ; l'en-tête d'application va juste après le charset.
anchor = re.search(r'<meta charset=[^>]*>', html)
assert anchor, 'charset introuvable dans plume.html'
html = html[:anchor.end()] + '\n' + HEAD + html[anchor.end():]
html, n = SAMPLE_AI.subn(SAMPLE_NO_AI, html)
assert n == 1, 'section IA du texte d\'exemple introuvable'
# Le nom affiché : World
for old, new in [('<title>Plume</title>', '<title>World</title>'),
                 ('<h1>Bienvenue dans Plume</h1>', '<h1>Bienvenue dans World</h1>'),
                 ("'Plein écran : Plume seule, sans la barre de Claude'", "'Plein écran'"),
                 ('avec mode concentration, Claude intégré (relecture, écriture, questions) et formules LaTeX.', 'avec mode concentration et formules LaTeX.')]:
    assert html.count(old) == 1, old
    html = html.replace(old, new)


if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
(OUT / 'index.html').write_text(html, encoding='utf-8')
for f in SRC.iterdir():
    if f.name != 'sw.js':
        shutil.copy(f, OUT / f.name)

# Le cache hors ligne change de nom à chaque nouvelle version, pour que l'app se mette à jour.
version = hashlib.sha1(b''.join((OUT / n).read_bytes() for n in sorted(p.name for p in OUT.iterdir()))).hexdigest()[:10]
(OUT / 'sw.js').write_text((SRC / 'sw.js').read_text(encoding='utf-8').replace('__VERSION__', version), encoding='utf-8')
(OUT / '.nojekyll').write_text('')
print('World prêt dans docs/ · version', version, '·', ', '.join(sorted(p.name for p in OUT.iterdir())))
