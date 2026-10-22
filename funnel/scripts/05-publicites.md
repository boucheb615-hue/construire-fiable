# Publicités Feed (FB/IG) · Facebook Newsfeed Ad Scripts AE (+ Conversion Ad Script Free, Curiosity Ad Copy Scripts AE)

Plateforme : Feed Facebook/Instagram. Limites (skill copy-ads) : environ 125 caractères visibles avant « Voir plus », titre d'environ 40 caractères. Trois annonces froides vers l'aimant (A, B, C), une annonce de reciblage vers la page de vente (D). Brief : `.copy/brief.yml`. Épine : `FUNNEL.md` (Épine v2).

## 1. Gabarit (extrait verbatim du corpus, en anglais, avec ses {variables})

Source principale : `facebook-newsfeed-ad-scripts-ae.md` (section Output).

```text
Primary Text
(Part 1) Watch this free video that reveals how you can gain an unfair advantage with {kwfocus1} and avoid {no1pain}.
(Part 2) Watch this free video to learn how we {problem1} to {immediateresult1}
------------
(Headline) Want To {problem1}? {targettitle} Helps.

Primary Text (Part 1) - Pick One
Here's the real reason you {kwfocus1} is failing (and x things you can do to change that right now)...
Don't let {no1pain} stop you from {no1desire}.
When pro {identity}s have {kwfocus1} problems, here's what they do.
Stop {no1pain} with {targettitle} or your money back.
How {identity}s can stop {no1pain} to {no1desire}.
{no1desire} with {targettitle} or your money back.
Answered: your most burning questions about how to {no1desire}.
```

Source secondaire : `conversion-ad-script-free.md` (reciblage, forme « Why are {identityp} thrilled… ») :

```text
Why are {identityp} thrilled about this {kwfocus1} {targettype}??
Because it's the fastest way to {bottomline1}!
{targettitle} gives you the tools you need to {no1desire} without {no1pain}.
Learn more here >>> LINK
```

Source tertiaire : `curiosity-ad-copy-scripts-ae.md` (forme « {kwfocus2} EXPOSED / Do NOT try until you read… », retenue pour l'idée de tension, non utilisée telle quelle : elle exige un « secret » et une personne, banni ou absent du brief).

## 2. Variables remplies

| variable | question du script | valeur en français | champ du brief |
|---|---|---|---|
| `kwfocus1` | mot-clé principal de l'annonce | agents de code fiables | `topic.focus` |
| `identity` / `identityp` | public (singulier / pluriel) | entrepreneur non technique / entrepreneurs non techniques | `audience.singular` / `audience.plural` |
| `immediateresult1` | résultat immédiat voulu | savoir si votre agent a vraiment fait ce qu'il annonce | `lead_magnet.promise` |
| `problem1` | problème à résoudre | l'agent annonce une correction qui n'a pas eu lieu | `pain.problems[0]` |
| `targettitle` (froid) | nom de ce qu'ils téléchargent | Le Test à l'Aveugle | `lead_magnet.title` |
| `targettitle` (reciblage) | nom de ce qu'ils achètent | Construire Fiable | `offer.name` |
| `targettype` | ce qui contient la solution | une checklist et un prompt à copier (froid) ; une cohorte en direct (reciblage) | `lead_magnet.type` ; `offer.type` |
| `unusualthingdescriptor` | description qui éveille la curiosité | un contrôle qualité qui ne demande pas de savoir coder | `offer.descriptor` |
| `no1desire` | gros gain | livrer un logiciel fiable sans devenir développeur | `desire.top` |
| `wandword` | quand ils obtiennent le gain | non utilisé (aucun délai de résultat prouvé) | `outcome.timeframe` (absent) |
| `timeframe` | délai | non utilisé (S4 : aucun délai de résultat promis) ; « 10 minutes » = durée de la checklist | `lead_magnet.promise` |
| `no1pain` | obstacle à éviter | croire l'agent quand il dit « terminé » | `pain.top` |
| `bottomline1` | ce qu'ils veulent pouvoir faire au final | mettre votre application entre les mains de vrais clients | `desire.others[2]` (reformulé) |
| `enemies` | ennemi (pluriel) | les promesses du « une application en 5 minutes » | `enemies` |

Champs du brief non utilisés : `testimonials` (vide, aucune preuve sociale), `outcome.timeframe` (absent).

## 3. Version remplie brute (gabarit traduit, variables en **gras**, avant réécriture)

**Annonce A (Part 1 + Part 2, froid)**
> Regardez cette vidéo gratuite qui révèle comment prendre un avantage sur **agents de code fiables** et éviter **croire l'agent quand il dit « terminé »**.
> Regardez cette vidéo gratuite pour apprendre comment nous **l'agent annonce une correction qui n'a pas eu lieu** pour **savoir si votre agent a vraiment fait ce qu'il annonce**.
> (Titre) Envie de **l'agent annonce une correction qui n'a pas eu lieu** ? **Le Test à l'Aveugle** aide.

**Annonce B (réponse « Answered »)**
> Réponse : vos questions les plus brûlantes sur comment **livrer un logiciel fiable sans devenir développeur**.

**Annonce C (« Don't let… stop you »)**
> Ne laissez pas **croire l'agent quand il dit « terminé »** vous empêcher de **livrer un logiciel fiable sans devenir développeur**.

**Annonce D (Conversion Ad Script Free, reciblage)**
> Pourquoi des **entrepreneurs non techniques** sont-ils ravis de cette **cohorte en direct** sur **agents de code fiables** ? Parce que c'est le plus court chemin pour **mettre votre application entre les mains de vrais clients**. **Construire Fiable** vous donne les outils pour **livrer un logiciel fiable sans devenir développeur**, sans **croire l'agent quand il dit « terminé »**.

Défauts relevés : la formule « vidéo gratuite » ne correspond à rien (l'aimant est une checklist) ; « avantage déloyal » et « aller plus vite » promettent plus que les preuves ; « le plus court chemin » n'est pas prouvé. Tout est réécrit.

## 4. Version finale (réécrite selon Jim Edwards)

Cadre commun : froid = PAS léger (problème : l'agent dit « terminé » sans l'avoir fait ; agitation : plus de corrections qui cassent d'autres choses ; solution : un second agent qui n'a rien vu), FAB en « Et alors ? » ×2, une accroche nommée par annonce, relances entre paragraphes, appel à l'action à verbe d'abord avec sa raison. Aucun prix dans les annonces froides. Titre froid retenu dans `01-titres.md` : « Faites le test à l'aveugle (10 min) » (35 caractères). La promesse de l'aimant (« savoir si votre agent a vraiment fait ce qu'il annonce… même si vous ne savez pas coder ») est reprise dans chaque corps.

### Annonce A · froide · accroche : Story
Accroche (visible avant « Voir plus ») : « Chez nous, une tâche est revenue « succeeded », code de sortie 0. L'agent n'avait rien fait. » (92 caractères)

> Chez nous, une tâche est revenue « succeeded », code de sortie 0. L'agent n'avait rien fait.
>
> Il avait démarré, n'avait reçu aucune consigne et s'était arrêté. Tout était vert.
>
> Ce jour-là, nous avons arrêté de croire les statuts.
>
> Depuis, chaque chose que nos agents construisent passe devant un second agent qui n'a rien vu de la construction. Il vérifie contre des critères écrits à l'avance. C'est le test à l'aveugle.
>
> Et alors ? Vous savez ce qui est prouvé et ce qui ne l'est pas. Et alors ? Vous n'avez plus à croire l'agent sur parole.
>
> Téléchargez Le Test à l'Aveugle (gratuit) : une checklist et un prompt à copier. Dix minutes, aucune ligne de code à lire, même si vous ne savez pas coder.

- [accroche : Story] [PAS · problème : l'agent dit « terminé » sans rien avoir fait] [PAS · agitation : « Tout était vert. »] [PAS · solution : le second agent] [FAB · fonction : second agent qui n'a rien vu ; avantage : vous savez ce qui est prouvé ; bénéfice : ne plus croire sur parole] [relance : « Et alors ? »] [CTA verbe d'abord + raison : « gratuit… dix minutes »]
- Titre : Faites le test à l'aveugle (10 min) (35) · Description : Checklist et prompt gratuits · Bouton : Télécharger · Lien : https://boucheb615-hue.github.io/construire-fiable/test-aveugle.html

### Annonce B · froide · accroche : Question
Accroche : « Comment savoir si votre agent a vraiment corrigé le bug, sans lire une ligne de code ? » (86 caractères)

> Comment savoir si votre agent a vraiment corrigé le bug, sans lire une ligne de code ?
>
> Vous écrivez « corrige ça ». L'agent répond « c'est fait ». Vous réessayez. Il corrige une chose et en casse dix.
>
> Vous voyez le problème ? Changer d'outil ne règle pas un « terminé » que personne n'a vérifié.
>
> Un agent qui relit son propre travail valide ses propres erreurs. Alors nous envoyons un second agent, qui n'a rien vu, vérifier contre des critères écrits à l'avance.
>
> Et alors ? Vous savez quoi corriger en premier. Et alors ? Vous sortez du tape-taupe.
>
> Téléchargez Le Test à l'Aveugle (gratuit) : la checklist et le prompt à copier, pour savoir en 10 minutes si votre agent a vraiment fait ce qu'il annonce. Même si vous ne savez pas coder.

- [accroche : Question] [PAS · problème : « corrige ça » en boucle ; agitation : « Il corrige une chose et en casse dix. » ; solution : le second agent] [relance : « Vous voyez le problème ? »] [FAB · fonction : critères écrits à l'avance ; avantage : vous savez quoi corriger en premier ; bénéfice : sortir du tape-taupe] [CTA verbe d'abord + raison]
- Titre : Faites le test à l'aveugle (10 min) (35) · Description : Gratuit · même sans savoir coder · Bouton : Télécharger · Lien : https://boucheb615-hue.github.io/construire-fiable/test-aveugle.html

### Annonce C · froide · accroche : Command
Accroche : « Arrêtez de croire l'agent quand il dit « terminé ». » (51 caractères ; l'accroche tient seule, la suite arrive après « Voir plus »)

> Arrêtez de croire l'agent quand il dit « terminé ».
>
> Chez nous, 11 textes marketing, chacun validé par sa propre vérification, contenaient 7 contradictions une fois lus ensemble.
>
> Vous voyez le problème ? Chaque contrôle regardait son morceau. Personne ne regardait l'ensemble.
>
> Demander à l'agent de vérifier son propre travail : il valide ses propres erreurs. Envoyer un second agent qui n'a rien vu : il lit comme un client.
>
> Et alors ? Vous voyez ce qui est prouvé avant de cliquer sur « publier ». Et alors ? Vous cliquez sur « publier » sans croiser les doigts.
>
> Téléchargez Le Test à l'Aveugle (gratuit) : la checklist et le prompt à copier. Faites-le aujourd'hui, même si vous ne savez pas coder.

- [accroche : Command] [PAS · problème : confiance au « terminé » ; agitation : 7 contradictions malgré 11 validations ; solution : second agent] [relance : « Vous voyez le problème ? »] [comparaison interne : l'agent qui relit son travail contre le second agent qui n'a rien vu] [FAB · bénéfice : publier sans croiser les doigts] [CTA verbe d'abord + raison : « aujourd'hui »]
- Titre : Faites le test à l'aveugle (10 min) (35) · Description : Checklist et prompt à copier · Bouton : Télécharger · Lien : https://boucheb615-hue.github.io/construire-fiable/test-aveugle.html

### Annonce D · reciblage · accroche : Comparison
Accroche : « Un prompt sur un exemple, ou le test à l'aveugle sur votre projet ? Vous avez le premier. Voici le second. » (106 caractères)

> Un prompt sur un exemple, ou le test à l'aveugle sur votre projet ? Vous avez le premier. Voici le second.
>
> Construire Fiable : 4 semaines en direct pour passer une fonctionnalité de VOTRE projet au test à l'aveugle, avec nous. 30 places seulement, car nous relisons chaque rapport de test à la main.
>
> Ce que vous recevez, avec sa valeur (chaque élément est vendu seul chez WebModerne) :
> • 4 ateliers en direct de 90 minutes : 388 €
> • 4 revues écrites de vos rapports de test : 188 €
> • Le kit Preuve : 47 €
> • Bonus 1, le pack 30 prompts de vérification : 27 €
> • Bonus 2, le guide « Brancher le second agent » : 27 €
> • Bonus 3, l'atelier de questions-réponses du lundi 14 décembre 2026 : 97 €
> • Le groupe Facebook privé des bâtisseurs fiables : offert
>
> Valeur totale : 774 €. Votre prix : 297 € (prix de la cohorte fondatrice ; il passe à 497 € à la cohorte suivante).
>
> Et ce n'est pas tout. Garantie Preuve : si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles.
>
> C'est la première cohorte : nous n'avons aucun témoignage, et nous ne l'inventons pas. Notre preuve : un premier agent vierge, lancé à l'aveugle sur notre outil copy-funnel, a trouvé les 6 pièges que nous avions cachés dans le brief de test.
>
> Séances les lundis 16, 23, 30 novembre et 7 décembre 2026 à 19h00 (heure de Paris). Inscriptions fermées le vendredi 13 novembre 2026 à 23h59.
>
> Réservez votre place avant le vendredi 13 novembre à 23h59 : après cette heure, les inscriptions sont fermées.
>
> P.S. Réservez votre place maintenant : le prix de 297 € s'arrête avec cette cohorte, et la Garantie Preuve couvre votre risque.

- [accroche : Comparison : un prompt sur un exemple contre le test à l'aveugle sur votre projet ; le prompt est déjà gratuit, nous vendons l'application à VOTRE projet, les revues et la cohorte, jamais un truc caché (S5)] [Hook-Story-Offer condensé : accroche, preuve et honnêteté (première cohorte), offre] [pile de valeur avec base : prix de chaque élément vendu seul chez WebModerne] [relance : « Et ce n'est pas tout. »] [rareté réelle : 30 places, avec sa raison] [urgence réelle : clôture le vendredi 13 novembre 2026 à 23h59, avec sa raison : prix de la cohorte fondatrice] [CTA verbe d'abord, répété avec une raison dans le P.S.]
- Titre : Construire Fiable · 30 places · 297 € (37) · Description : Valeur 774 € · clôture le 13 novembre · Bouton : S'inscrire · Lien : https://boucheb615-hue.github.io/construire-fiable/

## 5. Contrôle

**Accroches (premier paragraphe) et longueurs**

| annonce | caractères de l'accroche | tient avant « Voir plus » (125) | titre (≈ 40) | longueur totale du texte |
|---|---|---|---|---|
| A | 92 | oui | 35 | 701 |
| B | 86 | oui | 35 | 742 |
| C | 51 | oui | 35 | 704 |
| D | 106 | oui | 37 | 1737 |

**Chiffres et sources**

| chiffre / fait | annonce | source |
|---|---|---|
| « succeeded », code de sortie 0, l'agent n'avait rien fait | A | `constraints.proof[0]` ; `author.background` |
| 11 textes marketing, 7 contradictions | C | `constraints.proof[3]` |
| 6 pièges cachés trouvés par un agent vierge | D | `constraints.proof[2]` ; ligne de preuve de l'épine |
| 10 minutes | A, B, titres froids | `lead_magnet.promise` (durée de la checklist, pas un résultat client) |
| 4 ateliers de 90 minutes · 388 € | D | épine v2 (4 × 97 €) |
| 4 revues écrites · 188 € | D | épine v2 (4 × 47 €) |
| Le kit Preuve · 47 € | D | épine v2 |
| Bonus : 27 € + 27 € + 97 € | D | épine v2 |
| Valeur totale 774 € | D | 388 + 188 + 47 + 27 + 27 + 97 = 774 ; base annoncée : « chaque élément est vendu seul chez WebModerne » |
| 297 € ; 497 € ensuite | D | épine v2 (prix de la cohorte fondatrice) |
| 30 places | D | `event.capacity` ; raison : revue manuelle de chaque rapport |
| clôture le vendredi 13 novembre 2026 à 23h59 | D | `offer.deadline` |
| lundis 16, 23, 30 novembre, 7 décembre 2026, 19h00 ; bonus lundi 14 décembre 2026 | D | `event.*`, épine v2 |
| groupe Facebook privé : offert, sans valeur | D | `offer.extras` (hors du total) |

**Garantie, mot pour mot** : 0 citation dans A, B, C (aucun prix dans le froid) ; 1 citation dans D (précédée de « Garantie Preuve : »). Le P.S. de D la mentionne par son nom sans la reformuler. Texte cité : « si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles. »

**Autres contrôles**
- Aucun témoignage ; D dit qu'il n'y en a pas (première cohorte) et le remplace par `constraints.proof[2]`.
- Aucune promesse de résultat au-delà de la Garantie Preuve ; la méthode n'est jamais présentée comme supprimant tous les bugs.
- Aucun prix payant dans A, B, C. Aucune date d'ouverture inventée.
- Valeur totale annoncée avec sa base (D). Bonus nommés avec leur valeur (D, trois).
- Mots bannis (mots entiers : on, révolutionnaire, hack, magique, facile, garanti, secret) : voir sortie `fr_check` ci-dessous ; aucun dans les textes finaux. « Garantie » (nom) n'est pas « garanti ».
- Pronom interdit : aucun ; « nous » partout ; vouvoiement.
