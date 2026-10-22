# Construire Fiable · plan de tunnel (copy-funnel)

Brief : `.copy/brief.yml` · validateur : `valid: 5/5 required fields, 0 warnings`.
Trafic : froid, Facebook et Instagram (fil d'actualité). Langue : français.

## Étape 1 · Type de tunnel

| type | statut | raison |
|---|---|---|
| Aimant à prospects | **choisi** | trafic froid ; `lead_magnet` rempli (Le Test à l'Aveugle) |
| Tripwire | bloqué | aucun produit d'appel désigné |
| VSL | débloqué, non retenu | repli seulement |
| Webinaire | bloqué | pas de webinaire ; la cohorte n'est pas un webinaire |
| Lancement | bloqué | pas de liste existante déclarée |
| High-ticket | bloqué | pas de `offer.ladder[]` |

## Étape 2 · Carte du tunnel

| étape | contenu | skill → structure | statut | événement suivi |
|---|---|---|---|---|
| 1 | publicités FB/IG | `copy-ads` → Feed (FB/IG) | ready | `ad_click` |
| 2 | page d'inscription | `copy-sales-page` → Opt-in page | ready | `optin` |
| 3 | page de remerciement + mention de l'offre | `copy-offer` → Who-what-why-how | ready | `offer_view` |
| 4 | e-mails de livraison (3) | `copy-emails` → Lead-magnet delivery | ready | `lm_open` |
| 5 | histoire pont (dans l'e-mail 3) | `copy-story` → Epiphany Bridge, short | ready | — (vit dans l'étape 4) |
| 6 | e-mails jusqu'à la clôture (5) | `copy-emails` → Product launch **(écart, voir note)** | ready | `click_to_offer` |
| 7 | page de vente | `copy-sales-page` → Long-form letter | ready | `purchase` |
| 7a | offre + appel à l'action | `copy-offer` → Value stack, CTA block | ready | `checkout_start` |
| 7b | option au paiement | `copy-offer` → Order bump | ready | `bump_accept` |
| 8 | offre après achat | `copy-offer` → OTO: done-with-you | ready | `oto_accept` |
| 9 | e-mails d'accueil | `copy-emails` → Onboarding | non construit (hors demande) | `first_login` |

Note sur l'étape 6 : la carte « aimant à prospects » prévoit une séquence
Nurture. L'offre a une vraie date de clôture (13 novembre), donc la séquence
Product launch sert mieux. Écart signalé comme retour pour le skill.

## Étape 3 · Épine (verrouillée)

| ligne | valeur | source |
|---|---|---|
| promesse | ne livrer que ce qui est prouvé : chaque fonctionnalité passe un test à l'aveugle avant d'arriver chez vos clients | `outcome.payoff` réécrit (S8) |
| mécanisme | le test à l'aveugle | `offer.mechanism` |
| public | entrepreneurs non techniques | `audience.plural` |
| prix | 297 € aujourd'hui ; 497 € ensuite ; raison : prix de la cohorte fondatrice, il passe à 497 € à la cohorte suivante | `offer.price.*`, `offer.pricedrop_reason` |
| date limite | inscriptions fermées le vendredi 13 novembre 2026 à 23h59 (heure de Paris) | `offer.deadline` |
| places | 30 places (nous relisons chaque rapport de test à la main) | `event.capacity` |
| garantie | si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles. | `offer.guarantee` (mot pour mot) |
| ligne de preuve | un premier agent vierge, lancé à l'aveugle sur notre outil copy-funnel, a trouvé les 6 pièges que nous avions cachés dans le brief de test | `constraints.proof[2]` |
| séances | les lundis 16, 23, 30 novembre et 7 décembre 2026, 19h00 (heure de Paris), en visio | `event.*` |

Sous-épine option : Le pack 30 prompts de vérification · 27 € · pas de prix barré.
Sous-épine OTO : La Revue Preuve en duo · 197 € seul (aucun prix barré, aucune
garantie annoncée, S6) · portée : deux visios de 45 minutes sur VOTRE projet.

### Contrôles de l'épine

| id | résultat | détail |
|---|---|---|
| S1 | ok | une seule fin, datée ; la raison (« cohorte suivante ») ne fixe pas d'autre date |
| S2 | ok | la raison ne cite aucun livrable absent de l'offre |
| S3 | ok | aucune valeur annoncée, donc aucun total ni ancrage à justifier |
| S4 | ok | aucun délai de résultat promis ; « 10 minutes » de l'aimant = durée de la checklist, pas un résultat client |
| S5 | **conflit (b)** | l'aimant donne le prompt du test à l'aveugle, donc le mécanisme. Décision : la page de vente ne vend jamais « le secret » ; elle vend l'application sur VOTRE projet, la revue chaque semaine et la cohorte |
| S6 | ok après défaut | l'OTO n'a ni prix barré ni garantie : 197 € seul, aucune promesse de remboursement |
| S7 | ok | trafic froid avec aimant à prospects |
| S8 | **réécrit** | « livrer un logiciel qui fonctionne vraiment » promet un résultat sans preuve client (première cohorte). Promesse ramenée au processus vérifiable. Mots bannis vérifiés (mots entiers) |

## Règles de style (persona WebModerne)

- « nous », jamais « on ». Vouvoiement du lecteur.
- Espace (insécable) avant `?` `:` `!` `;`. Parenthèses plutôt que tirets.
- Pourcentages en chiffres avec `%`.
- Pas de « Imaginez la scène », pas d'analogie attendue. Rythme oral et court.
- Aucun témoignage inventé : c'est la première cohorte, nous le disons.
- Aucun chiffre hors `constraints.proof`.

## Épine v2 (révision après la revue de Karnon, prioritaire sur ce qui précède)

| ligne | valeur |
|---|---|
| titre page de vente | Enfin ! Comment livrer votre première fonctionnalité prouvée en 4 semaines… même si vous ne savez pas coder |
| pré-titre page de vente | Attention, entrepreneurs non techniques qui construisent avec Claude Code, Cursor, Lovable ou Bolt |
| sous-titre page de vente | Sans croire l'agent sur parole, sans lire une ligne de code, et sans corriger les mêmes bugs en boucle. |
| titre page d'inscription | Comment savoir si votre agent a vraiment fait ce qu'il annonce… même si vous ne savez pas coder |
| contenu (3 pièces) | 4 ateliers en direct de 90 minutes (388 €) · 4 revues écrites de vos rapports de test (188 €) · Le kit Preuve (47 €) |
| bonus (3) | Le pack 30 prompts de vérification (27 €) · Le guide « Brancher le second agent » (27 €) · L'atelier bonus de questions-réponses du lundi 14 décembre 2026 (97 €) |
| offert, sans valeur | le groupe Facebook privé des bâtisseurs fiables |
| valeur totale | 774 € (388 + 188 + 47 + 27 + 27 + 97) |
| base des valeurs | prix de chaque élément vendu seul chez WebModerne (à mettre en vente avant le lancement) |
| prix | 297 € aujourd'hui ; 497 € ensuite (prix de la cohorte fondatrice ; il passe à 497 € à la cohorte suivante) |
| option au paiement | Les replays à vie (27 €), au lieu de 12 mois |
| offre après achat | La Revue Preuve en duo (197 €, sans prix barré, sans garantie annoncée) |
| séances | les lundis 16, 23, 30 novembre et 7 décembre 2026, 19h00 (heure de Paris) ; atelier bonus le lundi 14 décembre 2026 |
| garantie | si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles. |

Cadre de rédaction : chaque texte part d'un script Funnel Scripts (gabarit à
variables, corpus `_wizard-corpus/`), variables remplies depuis le brief, puis
réécrit selon Jim Edwards (PAS, FAB, une des 11 accroches, Hook-Story-Offer,
relances entre paragraphes, P.S. systématique, appel à l'action répété avec
une raison).
