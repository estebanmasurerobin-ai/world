# World : ce que l'app sait lire (fiche pour préparer un document)

World (et Plume, et IA Writer) ouvrent quatre sortes de fichiers, depuis Documents › « Ouvrir depuis Fichiers… » :
**.md** (Markdown), **.html**, **.txt** et **.docx** (Word).

**Format conseillé : Markdown (.md).** Tout ce qui suit y est reconnu, LaTeX compris.
Pour des couleurs, surlignages, polices ou tailles, utiliser **.html** (voir plus bas).

## LaTeX : oui

- Les formules sont affichées par **MathJax 3** : presque tout le LaTeX mathématique marche,
  y compris `\frac`, `\sqrt`, `\sum`, `\int`, `\lim`, `\vec`, `\mathbb`, `\text`, les lettres grecques,
  `pmatrix`/`bmatrix`, `cases`, `aligned`.
- **En ligne :** `$e^{i\pi}+1=0$`.
- **Centrée sur sa ligne :** `$$\int_0^1 x^2\,dx = \frac13$$`. Elle peut tenir sur plusieurs lignes, entre deux lignes `$$`.
- **Écrire un vrai signe dollar :** `\$`.
- **Pas de LaTeX « de texte » :** `\section`, `\begin{document}`, TikZ, `\cite`… ne sont pas compris.
  On écrit le document en Markdown et on réserve le LaTeX aux formules.
- **Dans un .docx :** les équations de Word (éditeur d'équations) **ne sont pas reprises**.
  Les formules écrites en texte `$…$` dans le .docx, elles, deviennent de vraies formules.

## Markdown reconnu

| Élément | Écriture |
|---|---|
| Titres | `#`, `##`, `###` (3 niveaux ; `####` et plus deviennent `###`) |
| Gras / italique / barré | `**gras**`, `*italique*` ou `_italique_`, `~~barré~~` |
| Indice / exposant | `<sub>2</sub>`, `<sup>2</sup>` |
| Code | `` `code` `` en ligne ; bloc entre lignes ```` ``` ```` |
| Citation | `> texte` |
| Listes | `- ` ou `* ` ; numérotées `1. ` ; sous-listes avec 2 espaces d'indentation |
| Tâches | `- [ ] à faire`, `- [x] fait` |
| Tableau | lignes `\| a \| b \|` avec la ligne `\|---\|---\|` sous la première |
| Séparateur | `---` |
| Lien | `[texte](https://…)` |
| Image | `![](https://…)` ou image intégrée `data:image/png;base64,…` |
| Saut de ligne dans un paragraphe | deux espaces en fin de ligne |

**Ne passent pas en Markdown :** couleurs, surlignages, polices, tailles, alignement, notes de bas de page.

## HTML : toute la mise en forme de l'app

**Balises gardées :** `p h1 h2 h3 b strong i em u s del sub sup code pre blockquote ul ol li table thead tbody tr td th hr a img br span div`.
Tout le reste est enlevé : scripts, styles, formulaires…

| Effet | Attribut sur un `<span>` (ou un bloc) |
|---|---|
| Couleur du texte | `data-c="gris\|rouge\|orange\|jaune\|vert\|bleu\|violet\|rose\|marron"` |
| Surlignage | `data-h="<couleur> <style>"` : couleur `jaune vert bleu rose orange violet`, style `marqueur plein contour`. Exemple : `data-h="jaune marqueur"` |
| Soulignement | `data-u="simple\|double\|pointille\|tirets\|ondule\|epais"` |
| Police | `data-f="literata\|garamond\|lora\|playfair\|georgia\|times\|sourcesans\|atkinson\|nunito\|arial\|jetbrains\|courier\|caveat"` |
| Taille | `data-s="24" style="font-size:24px"`, à choisir parmi 12 14 16 18 20 22 24 28 32 40 48 64 |
| Formule | `<span class="math" data-tex="\frac{a}{b}"></span>`, avec `data-display="1"` pour la centrer |
| Alignement | `style="text-align:center"` (aussi `left`, `right`, `justify`) sur `p`, `h1`–`h3`, `li`, `td` |
| Retrait | `data-ind="1"` à `"4"` sur `p`, `h1`–`h3`, `blockquote` |
| Section repliée | `data-fold="1"` sur `h1`–`h3` |
| Liste de tâches | `<ul data-check>` puis `<li data-done="1">` pour une tâche faite |
| Liste numérotée | `<ol start="5">` pour commencer à 5 |
| Taille d'image | `data-w="s\|m\|l"` sur `img` |
| Note (commentaire) | `<span data-n="n1" data-nt="texte de la note">passage</span>` |

## Word (.docx)

**Repris :**
- paragraphes et titres ;
- gras, italique, barré, souligné, indices et exposants ;
- couleurs et surlignages (ramenés à la couleur de l'app la plus proche) ;
- tailles, listes, tableaux, images, liens ;
- cases ☐ ☑, qui deviennent des listes de tâches ;
- formules en `$…$`.

**Perdus :** équations Word, en-têtes et pieds de page, notes de bas de page, mise en page.

## Ce que l'app fait aussi (pas besoin de le préparer)

- **Organisation :** plan des titres, sections repliables, bibliothèque avec dossiers.
- **Suivi du texte :** historique des versions, mode révision (suivi des modifications), notes.
- **Écriture :** mode concentration, statistiques et objectif de mots, son de machine à écrire.
- **Export :** .docx, .md, .html, PDF (impression) et sauvegarde complète en .json.
