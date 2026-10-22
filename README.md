# Construire Fiable · le tunnel complet

Offre, pages, e-mails et publicités pour **Construire Fiable**, une cohorte
WebModerne de 4 semaines pour les entrepreneurs non techniques qui
construisent avec un agent de code (Claude Code, Cursor, Lovable, Bolt).

**Le site (GitHub Pages)** : https://boucheb615-hue.github.io/construire-fiable/

## Parcours à cliquer

1. Publicité → [page d'inscription à l'aimant](https://boucheb615-hue.github.io/construire-fiable/test-aveugle.html)
2. → [page de remerciement](https://boucheb615-hue.github.io/construire-fiable/merci.html) (confirmation + mention de l'offre)
3. → e-mail A2 → [Le Test à l'Aveugle](https://boucheb615-hue.github.io/construire-fiable/test-aveugle-kit.html) (l'aimant, utilisable tout de suite)
4. → e-mails → [page de vente](https://boucheb615-hue.github.io/construire-fiable/)
5. → [commande avec option à 27 €](https://boucheb615-hue.github.io/construire-fiable/commande.html) (démo, aucun paiement)
6. → [page après achat, offre à 197 €](https://boucheb615-hue.github.io/construire-fiable/merci-achat.html)

## Les textes

| fichier | contenu |
|---|---|
| [funnel/brief.yml](funnel/brief.yml) | le brief : public, offre, preuves autorisées |
| [funnel/FUNNEL.md](funnel/FUNNEL.md) | type de tunnel, carte des étapes, épine verrouillée, contrôles S1 à S8 |
| [funnel/offre.md](funnel/offre.md) | contenu de l'offre, appel à l'action, option, offre après achat, page de remerciement |
| [funnel/emails.md](funnel/emails.md) | 9 e-mails : livraison de l'aimant (3), compte à rebours (5), confirmation d'achat (1) |
| [funnel/publicites.md](funnel/publicites.md) | 4 publicités Facebook/Instagram (3 froides, 1 reciblage), avec la notation des accroches |
| [funnel/aimant-test-aveugle.md](funnel/aimant-test-aveugle.md) | l'aimant à prospects : checklist + prompt |
| [funnel/AUDIT.md](funnel/AUDIT.md) | l'audit à l'aveugle du tunnel : 7 FAIL trouvés et corrigés, ce qui reste ouvert |

## Les décisions

- **Offre** : cohorte en direct, 297 € (prix fondateur, 497 € ensuite), 30 places, inscriptions fermées le vendredi 13 novembre 2026 à 23h59 (heure de Paris).
- **Mécanisme** : le test à l'aveugle. Un second agent, qui n'a rien vu de la construction, vérifie le travail contre des critères écrits à l'avance.
- **Tunnel** : aimant à prospects pour le trafic froid (copy-funnel, départage « froid → aimant »).
- **Preuves** : uniquement le travail de WebModerne. Aucun témoignage inventé : c'est la première cohorte, et les pages le disent.

## Comment c'est fait

Construit avec les skills [funnel-script](https://github.com/Karnonson/funnel-script)
(branche `copy-funnel`, pas encore publiée) : copy-funnel pour la carte et l'épine, copy-offer,
copy-sales-page, copy-emails, copy-ads, puis un audit à l'aveugle par un agent
neuf. `tools/fr_check.py` vérifie la typographie française et les mots
bannis ; `tools/apply_audit_fixes.py` applique les corrections de l'audit.
