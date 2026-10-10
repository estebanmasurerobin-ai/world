# Plume et World

- **Plume** (`plume.html`) : l'éditeur, publié sur claude.ai avec Claude intégré (relecture, écriture, questions).
- **World** (`docs/`) : la même base d'éditeur en application autonome, **sans aucune intelligence artificielle**,
  installable sur l'écran d'accueil (icône, plein écran, fonctionne hors ligne). Publiée par GitHub Pages.

Fichiers :
- `world/` : ce qui fait de l'éditeur l'application World (icônes, manifeste, hors ligne).
- `build.py` : assemble World dans `docs/` à partir de `plume.html` (`python3 build.py`).
  Il renomme Plume en World, retire tout ce qui touche à l'IA et adapte le texte d'exemple.
