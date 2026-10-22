# Consignes communes aux rédacteurs (Construire Fiable, révision 2)

Lis d'abord, en entier : `/home/agentic/webmoderne-fiable/.copy/brief.yml`,
`/home/agentic/webmoderne-fiable/FUNNEL.md` (surtout la section « Épine v2 »,
prioritaire sur tout le reste), `/home/agentic/webmoderne-fiable/scripts/01-titres.md`
(titres déjà choisis : ne pas les changer), et le skill Jim Edwards
`/home/agentic/.hermes/skills/creative/jim-edwards-copywriting/SKILL.md`.
Les gabarits Funnel Scripts sont dans
`/home/agentic/funnel-script/.claude/skills/_wizard-corpus/<script>.md`
(section « Inputs » = variables, section « Output » = gabarit avec `{variables}`).

## Ce que la revue de Karnon exige

1. Chaque texte part d'un **script Funnel Scripts** : gabarit à variables, variables remplies depuis le brief, puis réécriture.
2. Le cadre de rédaction est **Jim Edwards** : PAS, FAB (« et alors ? » trois fois), une des 11 accroches nommée, Hook-Story-Offer pour le long, relances entre paragraphes (« Vous voyez le problème ? », « Et ce n'est pas tout. »), P.S. dans chaque e-mail et lettre, appel à l'action à verbe d'abord, répété avec une raison.
3. Les **bonus ont leur valeur en euros**, et la valeur totale (774 €) est annoncée, avec la base des valeurs.

## Format du document de script (un par livrable, dans `scripts/`)

```
# <Livrable> · <script(s) Funnel Scripts utilisé(s)>
## 1. Gabarit (extrait verbatim du corpus, en anglais, avec ses {variables})
## 2. Variables remplies   (tableau : variable | question du script | valeur en français | champ du brief)
## 3. Version remplie brute (gabarit traduit, variables remplacées en **gras**, avant réécriture)
## 4. Version finale        (réécrite selon Jim Edwards ; notes de cadre entre crochets, ex. [PAS · agitation], [FAB · sens], [accroche : Question])
## 5. Contrôle              (chaque chiffre et sa source ; nombre de citations de la garantie, mot pour mot ; mots bannis)
```

## Règles absolues

- Tout en **français**. « nous » pour WebModerne, **jamais le pronom « on »**. Vouvoiement.
- Espace insécable (U+00A0) avant `? : ! ;` et entre un nombre et `%` ou `€`. Parenthèses plutôt que tirets d'incise. Phrases courtes, orales, concrètes. Pas de « Imaginez la scène ».
- Mots bannis (mots entiers) : on, révolutionnaire, hack, magique, facile, garanti, secret.
- **Aucune preuve inventée.** Chiffres autorisés : `constraints.proof` (mot pour mot dans le sens, ex. « au moins 453 fois », « un service en double de notre passerelle »), l'épine v2 (prix, valeurs, dates, 30 places), `lead_magnet` (« 10 minutes » = durée de la checklist). C'est la première cohorte : aucun témoignage, et nous le disons quand un gabarit en demande un (remplacer le bloc témoignage par une preuve de `constraints.proof` ou par cette phrase honnête).
- Ne jamais dire que la méthode supprime tous les bugs. Aucune promesse de résultat client au-delà de la Garantie Preuve.
- **Garantie mot pour mot** partout où elle apparaît : « si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles. »
- Dates : inscriptions fermées le vendredi 13 novembre 2026 à 23h59 (heure de Paris) ; ateliers les lundis 16, 23, 30 novembre et 7 décembre 2026 à 19h00 ; atelier bonus le lundi 14 décembre 2026. Ne crée aucune autre date (pas de date d'« ouverture »).
- Liens : page de vente `https://boucheb615-hue.github.io/construire-fiable/` ; inscription à l'aimant `.../test-aveugle.html` ; livraison de l'aimant `.../test-aveugle-kit.html` ; commande `.../commande.html`.
- Le gratuit (Le Test à l'Aveugle) donne déjà le prompt : le payant se vend comme l'application à VOTRE projet, les revues et la cohorte, jamais comme « le secret ».
- N'écris que les fichiers qui te sont attribués. Ne modifie ni le brief ni FUNNEL.md.
- Vérifie à la fin avec : `python3 /home/agentic/webmoderne-fiable/tools/fr_check.py --fix <tes fichiers>` (il corrige les espaces et signale les mots bannis ; dans les sections 1 et 5, les signalements sur l'anglais du gabarit ou sur la liste des mots bannis sont acceptables).
