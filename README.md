# Plume et World

- **Plume** (`plume.html`) : l'éditeur, publié sur claude.ai avec Claude intégré (relecture, écriture, questions).
- **World** (`docs/`) : la même base d'éditeur en application autonome, **sans aucune intelligence artificielle**,
  installable sur l'écran d'accueil (icône, plein écran, fonctionne hors ligne). Publiée par GitHub Pages.

Fichiers :
- `world/` : ce qui fait de l'éditeur l'application World (icônes, manifeste, hors ligne).
- `build.py` : assemble World dans `docs/` à partir de `plume.html` (`python3 build.py`).
  Il renomme Plume en World, retire tout ce qui touche à l'IA et adapte le texte d'exemple.

Ce que font les deux applications (identiques, sauf l'IA réservée à Plume) :
- Barre simple : annuler/rétablir, style de paragraphe, police, taille, gras, italique, soulignement,
  couleur, surlignage, liste, menu **+** (formule, lien, image, tableau, liste de tâches, liste numérotée,
  bloc de code, séparateur) et menu **Aa** (barré, indice, exposant, alignement, retrait, pinceau, effacer).
- Menu **⋯** : onglets, rechercher et remplacer (aussi dans tous les onglets), plan du document,
  statistiques et objectif de mots, historique des versions, vérification du style ; sous-menus
  **Fichier** (ouvrir, enregistrer dans Fichiers, export PDF, Word, Markdown, HTML, sauvegarde complète)
  et **Mise en page** (thème, largeur, interligne, espacement, retrait, correcteur, majuscules automatiques).
- Mode concentration, machine à écrire, sections repliables, notes, formules LaTeX, habillage Liquid Glass.
