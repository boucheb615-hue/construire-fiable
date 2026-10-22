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

## Ouvert avant lancement

- Lien de paiement réel (Stripe ou équivalent) : les pages `commande.html` et `merci-achat.html` sont des démos.
- Le kit Preuve (3 modèles) reste à produire ; l'e-mail C1 porte des marqueurs `[lien du modèle]`.
- Outil d'envoi des e-mails (double opt-in, pied de page légal).
- Suivi des événements (A9) : aucun pixel ni événement branché.
- Groupe Facebook privé à créer.
