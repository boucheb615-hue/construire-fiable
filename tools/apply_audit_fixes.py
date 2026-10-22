#!/usr/bin/env python3
"""Apply the blind-audit fixes to the Construire Fiable funnel. Each
replacement must match exactly once (or the stated count) or the script
stops, so nothing is silently skipped."""
import pathlib, sys

R = pathlib.Path('/home/agentic/webmoderne-fiable')
BASE = 'https://boucheb615-hue.github.io/construire-fiable/'
SALES, OPTIN, KIT = BASE, BASE + 'test-aveugle.html', BASE + 'test-aveugle-kit.html'
CHECKOUT, OTO = BASE + 'commande.html', BASE + 'merci-achat.html'
G_OLD = 'si au 30e jour vous'
G_NEW = 'si au 30e jour après la première séance vous'


def edit(rel, pairs):
    p = R / rel
    t = p.read_text(encoding='utf-8')
    for old, new, n in pairs:
        c = t.count(old)
        if (n is None and c == 0) or (n is not None and c != n):
            sys.exit(f'{rel}: expected {n} of {old[:60]!r}, found {c}')
        t = t.replace(old, new)
    p.write_text(t, encoding='utf-8')
    print('ok', rel)


NB = '\u00a0'
# --- emails -------------------------------------------------------------
edit('out/emails.md', [
    ('- Aimant à prospects : https://webmoderne.github.io/test-aveugle [URL à confirmer]'.replace(' :', NB + ':'),
     f'- Page d\'inscription à l\'aimant{NB}: {OPTIN}\n- Page de livraison de l\'aimant (lien de l\'e-mail A2){NB}: {KIT}', 1),
    ('- Page de vente : https://webmoderne.github.io/construire-fiable [URL à confirmer]'.replace(' :', NB + ':'),
     f'- Page de vente{NB}: {SALES}\n\nRègle A3{NB}: après le vendredi 13 novembre 2026, supprimer les deux paragraphes sur la cohorte (inscriptions fermées).', 1),
    ('Le Test à l\'Aveugle, la checklist et le prompt à copier' + NB + ':\nhttps://webmoderne.github.io/test-aveugle',
     'Le Test à l\'Aveugle, la checklist et le prompt à copier' + NB + ':\n' + KIT, 1),
    ('Télécharger Le Test à l\'Aveugle (https://webmoderne.github.io/test-aveugle)',
     f'Ouvrir Le Test à l\'Aveugle ({KIT})', 1),
    ('Nous lisons chaque réponse.', 'Nous lisons les réponses.', 1),
    ('https://webmoderne.github.io/construire-fiable', SALES, None),
    # B1 / B2: no invented opening date
    ('| B1 | lundi 9 novembre 2026 (J-1) | prévenir que l\'ouverture est demain | Demain' + NB + ': Construire Fiable |',
     '| B1 | lundi 9 novembre 2026 (J-4) | annoncer le compte à rebours | Plus que 4 jours pour Construire Fiable |', 1),
    ('| B2 | mardi 10 novembre 2026 (ouverture) | présenter l\'offre complète et le prix | Construire Fiable est ouvert |',
     '| B2 | mardi 10 novembre 2026 (J-3) | présenter l\'offre complète et le prix | Construire Fiable, en détail |', 1),
    ('## B1 · J-1 (prévenir)', '## B1 · J-4 (compte à rebours)', 1),
    ('**Objet' + NB + ':** Demain' + NB + ': Construire Fiable', '**Objet' + NB + ':** Plus que 4 jours pour Construire Fiable', 1),
    ('**Préheader' + NB + ':** Pour ne livrer que ce qui est prouvé. L\'ouverture est demain.',
     '**Préheader' + NB + ':** Pour ne livrer que ce qui est prouvé. Fermeture vendredi soir.', 1),
    ('C\'est pour cela que nous avons préparé quelque chose. Il ouvre demain.',
     'C\'est pour cela que nous avons préparé quelque chose. Les inscriptions ferment vendredi.', 1),
    ('Demain, vous recevez le lien et tous les détails.', 'Demain, nous vous envoyons tous les détails. Le lien est déjà là.', 1),
    ('**CTA' + NB + ':** aucun lien aujourd\'hui. Action demandée' + NB + ': ouvrir l\'e-mail de demain.',
     f'**CTA{NB}:** Voir Construire Fiable ({SALES})', 1),
    ('## B2 · Ouverture', '## B2 · J-3 (l\'offre en détail)', 1),
    ('**Objet' + NB + ':** Construire Fiable est ouvert', '**Objet' + NB + ':** Construire Fiable, en détail', 1),
    ('Construire Fiable ouvre aujourd\'hui. L\'idée', 'Voici Construire Fiable en détail. L\'idée', 1),
    # B3: proof wording + outcome promise
    ('Chez nous, notre propre passerelle Telegram a redémarré en boucle 453 fois. La cause n\'était pas un bug de code. C\'était un service en double.',
     'Chez nous, un service en double de notre passerelle Telegram a redémarré en boucle au moins 453 fois, pendant que la vraie passerelle répondait normalement. La cause n\'était pas un bug de code. C\'était un service en double.', 1),
    ('Vous devenez un bâtisseur qui livre du logiciel fiable. Pas un développeur' + NB + ': un bâtisseur qui vérifie.',
     'Vous ne devenez pas développeur. Vous devenez quelqu\'un qui vérifie avant de croire.', 1),
    ('Construire Fiable vous donne les outils pour sortir de ce tape-taupe' + NB + ':',
     'Construire Fiable vous donne de quoi voir clair dans ce tape-taupe' + NB + ':', 1),
    (G_OLD, G_NEW, 3),
])

# --- sales page ---------------------------------------------------------
edit('out/landing/index.html', [
    ('Ce que le test à l\'aveugle a attrapé chez nous', 'Ce que nous avons observé chez nous', 1),
    ('Deux dates de fin pour la même offre. Une phrase d\'accroche qui promettait l\'envoi d\'une liste qui n\'existait pas.', '', 1),
    ('<strong>453 redémarrages.</strong>Un service en double de notre passerelle Telegram a redémarré en boucle au moins 453 fois, pendant que la vraie passerelle répondait normalement. Vu de l\'extérieur, tout marchait. C\'est en vérifiant au lieu de croire que la boucle est apparue.',
     '<strong>Au moins 453 redémarrages.</strong>Un service en double de notre passerelle Telegram a redémarré en boucle au moins 453 fois, pendant que la vraie passerelle répondait normalement. La cause était un service en double, pas un bug de code.', 1),
    ('L\'outil copy-funnel est passé par 3 tours de test à l\'aveugle avant d\'être livré. Chaque tour a trouvé ce que le précédent avait laissé passer.',
     'L\'outil copy-funnel est passé par 3 tours de test à l\'aveugle avant d\'être livré.', 1),
    ('C\'est la fin du tape-taupe' + NB + ': une correction qui casse autre chose est vue tout de suite.',
     'Si une correction casse autre chose, vous le voyez tout de suite, au lieu de le découvrir chez un client.', 1),
    ('href="#paiement"', f'href="{CHECKOUT}"', 1),
    ('le lundi à 19h00 (heure de Paris), à partir du 16 novembre 2026.',
     'les lundis 16, 23, 30 novembre et 7 décembre 2026 à 19h00 (heure de Paris).', 1),
    (' C\'est aussi la raison du prix fondateur.', '', 1),
    (G_OLD, G_NEW, None),
])

# --- offer pieces -------------------------------------------------------
edit('out/offer.md', [
    ('Des ateliers en visio, le lundi à 19h00 (heure de Paris), à partir du 16 novembre 2026.',
     'Des ateliers en visio, les lundis 16, 23, 30 novembre et 7 décembre 2026 à 19h00 (heure de Paris).', 1),
    (' Il répond à la peur de rester bloqué seul un mardi soir avec une appli cassée.', ' Personne ne reste bloqué seul entre deux séances.', 1),
    ('Le kit Preuve est déjà dans votre boîte mail, et nous nous retrouvons le lundi 16 novembre à 19h00.',
     'Le kit Preuve arrive dans votre boîte mail dans quelques minutes (e-mail C1), et nous nous retrouvons le lundi 16 novembre 2026 à 19h00.', 1),
    ('Une précision honnête sur ce que la cohorte fait et ne fait pas. La revue hebdomadaire est écrite' + NB + ': nous lisons le rapport du second agent sur votre projet et nous vous répondons. Pour la plupart des projets, c\'est suffisant. Certains projets ont besoin qu\'une personne regarde l\'application tourner, en direct, avec vous.',
     'Une précision honnête sur ce que la cohorte fait et ne fait pas. Les séances sont en groupe, et la revue hebdomadaire est écrite. Si votre projet a besoin d\'un tête-à-tête, où une personne regarde votre application tourner avec vous et vous seul, la cohorte ne le prévoit pas.', 1),
    ('**Pourquoi**' + NB + ': le test que vous venez de recevoir vous dit si l\'agent a menti. La cohorte vous apprend à construire pour qu\'il n\'ait plus l\'occasion de le faire sans que vous le sachiez.',
     '**Pourquoi**' + NB + ': le test que vous allez recevoir vous dit si l\'agent a menti sur une chose. La cohorte vous apprend à appliquer ce test à chaque fonctionnalité de votre projet.', 1),
    ('**C\'est parti. Le Test à l\'Aveugle arrive dans votre boîte mail.**',
     '**Dernière étape' + NB + ': confirmez votre adresse.** Ouvrez l\'e-mail que nous venons d\'envoyer et cliquez sur le lien. Le Test à l\'Aveugle arrive juste après.', 1),
    ('[Voir Construire Fiable]', f'[Voir Construire Fiable]({SALES})', 1),
    (G_OLD, G_NEW, 1),
])

# --- lead magnet + opt-in ------------------------------------------------
edit('out/lead-magnet-test-aveugle.md', [
    ('C\'est souvent là que l\'agent a triché.', 'C\'est là qu\'un agent peut tricher sans que vous le voyiez.', 1),
    ('Construire Fiable vous apprend à construire tout votre projet comme ça',
     'Construire Fiable vous apprend à appliquer ce test à chaque fonctionnalité de votre projet', 1),
    ('https://webmoderne.github.io/construire-fiable', SALES, 1),
])
edit('out/landing/test-aveugle.html', [
    ('Un e-mail avec le test, puis', 'Un e-mail pour confirmer votre adresse, puis le test, puis', 1),
    ('techniques : appliquez', 'techniques' + NB + ': appliquez', 0) if False else ('<meta name="description" content="La checklist', '<meta name="description" content="La checklist', 1),
])

# --- ads ------------------------------------------------------------------
edit('out/ads.md', [
    ('https://webmoderne.github.io/test-aveugle', OPTIN, None),
    ('https://webmoderne.github.io/construire-fiable', SALES, None),
])

# --- brief + funnel ---------------------------------------------------------
edit('.copy/brief.yml', [
    ('url: https://webmoderne.github.io/construire-fiable', f'url: {SALES}', 1),
    ('url: https://webmoderne.github.io/test-aveugle', f'url: {KIT}', 1),
    (G_OLD.replace(NB, ' '), G_NEW, 1),
    ('si au 30e jour vous n\'avez pas', 'si au 30e jour après la première séance vous n\'avez pas', 0) if False else ('date: lundi 16 novembre 2026', 'date: les lundis 16, 23, 30 novembre et 7 décembre 2026', 1),
])
edit('FUNNEL.md', [(G_OLD, G_NEW, 1),
                   ('| début | lundi 16 novembre 2026, 19h00 (heure de Paris), en visio |',
                    '| séances | les lundis 16, 23, 30 novembre et 7 décembre 2026, 19h00 (heure de Paris), en visio |', 1)])
print('all edits applied')
