# Audit à l'aveugle du tunnel

Le tunnel a été audité par un agent qui n'avait rien écrit (copy-funnel,
contrôles A1 à A9), contre le brief et l'épine verrouillée. Un piège témoin
était laissé exprès (formulation fausse de la preuve « 453 » dans l'e-mail
B3). L'auditeur l'a trouvé.

Résultat brut : **7 FAIL, 9 groupes de WARN**. Corrections ci-dessous.

## FAIL (tous corrigés)

| # | contrôle | problème trouvé | correction |
|---|---|---|---|
| 1 | A5 | e-mail B3 : la preuve « 453 » disait « notre passerelle a redémarré », sans « au moins » ni le fait que la vraie passerelle répondait | formulation exacte de la preuve |
| 2 | A5 | page de vente : la section « ce que le test à l'aveugle a attrapé » attribuait au test des choses que la preuve ne dit pas, et ajoutait des détails | titre « Ce que nous avons observé chez nous » ; détails non prouvés supprimés |
| 3 | A4 | bouton d'achat vers `#paiement`, qui n'existait pas | page `commande.html` (avec l'option à 27 €), puis `merci-achat.html` (offre à 197 €) |
| 4 | A4 | l'e-mail de livraison renvoyait au formulaire d'inscription | page de livraison `test-aveugle-kit.html` ; e-mail A2 et brief mis à jour |
| 5 | A2 / A4 | e-mails B1 et B2 annonçaient une « ouverture » le 10 novembre, alors que l'offre est visible avant | séquence B réécrite en compte à rebours vers la clôture ; règle d'envoi pour A3 après le 13 novembre |
| 6 | A4 | page après achat : « le kit est déjà dans votre boîte mail », mais aucun e-mail ne le livrait | e-mail C1 (confirmation d'achat + kit) |
| 7 | A8 / A5 | « Vous devenez un bâtisseur qui livre du logiciel fiable » et « c'est la fin du tape-taupe » promettaient un résultat | réécrits en processus : « vous le voyez tout de suite » |

## WARN traités

- Cadence des séances non sourcée : décidée et ajoutée au brief (les lundis 16, 23, 30 novembre et 7 décembre 2026).
- « Au 30e jour » sans point de départ : la garantie dit désormais « au 30e jour après la première séance », partout.
- Promesse trop large dans l'aimant et la page de remerciement (« tout votre projet ») : ramenée à « chaque fonctionnalité ».
- Deuxième raison du prix dans la FAQ : supprimée.
- Double opt-in non annoncé : page d'inscription et page de remerciement le disent.
- Offre à 197 € qui vendait contre les séances en direct : elle vend désormais le tête-à-tête, que la cohorte ne prévoit pas.
- « C'est souvent là que l'agent a triché » (fréquence non prouvée) : réécrit.
- Note de travail oubliée (« un mardi soir ») : supprimée.

## Révision 2 (après la revue de Karnon)

Retours : publicités et e-mails introuvables sur le site ; formule de titre mal appliquée ; bonus sans valeur ; scripts Funnel Scripts (gabarits à variables) et cadre Jim Edwards absents.

- Pages de revue ajoutées : `revue.html`, `annonces.html` (aperçu de fil), `emails.html` (aperçu de boîte mail), `scripts/`.
- Titres refaits à partir des formules Core, Killer et Million Dollar Sales, remplies et notées (4 U + contrôle Vrai).
- Offre refaite avec le script Offer Stack : 3 pièces + 3 bonus valorisés, valeur totale 774 €, base des valeurs annoncée.
- Option au paiement : « Les replays à vie » (27 €) ; l'ancien pack de prompts devient le bonus n°1.
- Chaque texte réécrit depuis son gabarit Funnel Scripts, avec un document de script en 5 sections (gabarit, variables, version brute, version finale, contrôle).

## Ouvert avant lancement

- **Mettre en vente seul, aux prix annoncés, chaque élément valorisé** (atelier 97 €, revue écrite 47 €, kit Preuve 47 €, pack de prompts 27 €, guide 27 €). Sinon la valeur totale de 774 € n'est pas défendable.
- Lien de paiement réel (Stripe ou équivalent) : les pages `commande.html` et `merci-achat.html` sont des démos.
- Le kit Preuve (3 modèles), le guide et le pack de prompts restent à produire ; l'e-mail C1 porte des marqueurs `[lien du modèle]`.
- Outil d'envoi des e-mails (double opt-in, `[prénom]`, pied de page légal).
- Visuels des publicités (les aperçus utilisent un fond provisoire).
- Suivi des événements (A9) : aucun pixel ni événement branché.
- Groupe Facebook privé à créer.
