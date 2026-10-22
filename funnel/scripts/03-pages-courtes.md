# 03 · Pages courtes (Construire Fiable)

Cadre : Jim Edwards (PAS, FAB, une accroche nommée, relances, P.S., appel à l'action à verbe d'abord avec une raison). Épine v2 prioritaire. Quatre pages : inscription, remerciement, commande avec bump, OTO. Fichiers HTML : `out/landing/`.

# Partie A · Page d'inscription (test-aveugle.html) · lead-capture-script-free + lead-capture-script-2

## 1. Gabarit (extrait verbatim du corpus, en anglais, avec ses {variables})

```text
### lead-capture-script-free

{leadmagnettitle}


"How To {desire1}"



Enter your best email below and I'll send you a FREE copy of my new {thing} "{leadmagnettitle}"





YES ! I Want To {bottomline1} Immediately



Exclusive {thing} Reveals The Greatest Method in The World To {desire1}... The Easy Way !


Here's a taste of what you get in {leadmagnettitle}:

* Your easy button to {immediateresult1} - Immediately !

* Escape {no1pain} trying to {bottomline1}

* How to {desire1} - No experience required !

* Swiftly {problem1}... even if you've never done it before

* Identify the amazing resources to {no1desire}

* STOP needless stress over {kwfocus1} - For Life !


Claim Your Free Copy Today !


YES ! I Want To {bottomline1} Immediately

### lead-capture-script-2 (Basic Opt-in, sans vidéo)

Basic Opt-in /Squeeze Page Template Draft with NO Video or Audio


"{howtosecret}"

* {bigresult}

* {bigprize}

* {salespagetakeaway}

Hi, my name is {name} and welcome to {website}.

In the next few minutes you are going to discover how to {bigresult} just like {targetniche} from all over the country/world.

We've even put together a {whatget} showing you {bigprize}.

Just enter your first name, your email address and click the "Send My {whatget}" button below and you'll instantly receive the {whatget} by return email.

Also, on the next page, you'll receive all the information that shows you {howtosecret}.

So go ahead... enter your first name, your email address and click the "Send My {whatget}" button to instantly receive the {whatget} by return email.



YES ! I'm ready to discover {howtosecret} and {bigresult}! Please send my {whatget} now...





	
{whatget} Now" />



We respect your email privacy !




---------------------------------------------------------------------------------
Contact information and disclaimer links
(c) Copyright - {name} - All Rights Reserved
```

## 2. Variables remplies

| variable | question du script | valeur en français | champ du brief |
|---|---|---|---|
| `leadmagnettitle` | What is the title of your lead magnet ? | Le Test à l'Aveugle | `lead_magnet.title` |
| `thing` | What type of lead magnet are you offering ? | checklist et prompt à copier | `lead_magnet.type` |
| `desire1` | #1 long-term desire (VERB) | savoir si votre agent a vraiment fait ce qu'il annonce… même si vous ne savez pas coder (titre imposé, 01-titres.md §3) | `desire.top` réécrit (S8) ; `lead_magnet.promise` |
| `bottomline1` | #1 thing your avatar wants to be able to do | savoir ce qui est prouvé et ce qui ne l'est pas dans votre projet | `outcome.supporting[1]` |
| `immediateresult1` | #1 immediate result | savoir en 10 minutes si votre agent a vraiment fait ce qu'il annonce | `lead_magnet.promise` |
| `no1pain` | #1 pain avoided (ING) | croire l'agent sur parole | `pain.top` |
| `problem1` | #1 problem to solve | sortir du « corrige ça » en boucle | `audience.vocabulary[0]` |
| `roadblock1` | #1 objection | il faut savoir coder pour vérifier | `pain.false_belief` |
| `no1desire` | #1 result from the offer (VERB) | contrôler le travail de l'agent sans lire une ligne de code | `benefits[0]` |
| `kwfocus1` | main topic | agent de code | `topic.focus` |
| `timeframe` | timeframe | 10 minutes (durée de la checklist ; pas un résultat client) | `lead_magnet.promise` |
| `name` / `website` | (lead-capture-script-2) your name / website | WebModerne | `author.company` |
| `whatget` | (lead-capture-script-2) bribe | Le Test à l'Aveugle | `lead_magnet.title` |
| `bigprize` | (lead-capture-script-2) payoff of the bribe | savoir en 10 minutes si votre agent a vraiment fait ce qu'il annonce | `lead_magnet.promise` |
| `salespagetakeaway` | (lead-capture-script-2) reveal made one page later | la cohorte Construire Fiable, qui applique le test à votre projet | `offer.what_it_is` |

## 3. Version remplie brute (gabarit traduit, variables remplacées en **gras**, avant réécriture)

Le Test à l'Aveugle

« Comment **savoir si votre agent a vraiment fait ce qu'il annonce… même si vous ne savez pas coder** »

Entrez votre meilleure adresse e-mail ci-dessous et nous vous envoyons un exemplaire GRATUIT de notre nouvelle **checklist et prompt à copier** « **Le Test à l'Aveugle** »

OUI ! Je veux **savoir ce qui est prouvé et ce qui ne l'est pas dans mon projet** immédiatement

Cette **checklist et prompt à copier** exclusive révèle la meilleure méthode du monde pour **savoir si votre agent a vraiment fait ce qu'il annonce**... la méthode la plus directe !

Voici un aperçu de ce que vous obtenez dans Le Test à l'Aveugle :

* Votre raccourci pour **savoir en 10 minutes si votre agent a vraiment fait ce qu'il annonce** - immédiatement !
* Échappez à **croire l'agent sur parole** en essayant de **savoir ce qui est prouvé dans votre projet**
* Comment **savoir si votre agent a vraiment fait ce qu'il annonce** - aucune expérience requise !
* Rapidement **sortir du « corrige ça » en boucle**... même si vous ne l'avez jamais fait
* Identifiez les ressources étonnantes pour **contrôler le travail de l'agent sans lire une ligne de code**
* ARRÊTEZ le stress inutile autour de **l'agent de code** - pour la vie !

Réclamez votre exemplaire gratuit aujourd'hui !

OUI ! Je veux **savoir ce qui est prouvé et ce qui ne l'est pas dans mon projet** immédiatement

(Squeeze page, lead-capture-script-2 : « Dans les prochaines minutes, vous allez découvrir comment **savoir en 10 minutes si votre agent a vraiment fait ce qu'il annonce** comme **les entrepreneurs non techniques** du monde entier. Nous avons même préparé **Le Test à l'Aveugle** qui vous montre **savoir en 10 minutes…** Entrez votre e-mail et cliquez sur « Envoyez-moi **Le Test à l'Aveugle** ». Sur la page suivante, **la cohorte Construire Fiable**. »)

## 4. Version finale (réécrite selon Jim Edwards)

```text
[pré-titre (lead-magnet title, 01-titres.md §3)]
Le Test à l'Aveugle · gratuit · 10 minutes

[titre · accroche nommée : How To (« How To {desire1} »), 01-titres.md §3 exactement]
Comment savoir si votre agent a vraiment fait ce qu'il annonce… même si vous ne savez pas coder

[PAS · problème]
Votre agent écrit « terminé ». L'écran est tout vert. Et vous n'avez aucun moyen de vérifier sans lire le code.

[PAS · agitation (constraints.proof[0])]
Chez WebModerne, une tâche confiée à un agent a renvoyé « succeeded », code de sortie 0, sans avoir rien fait. Tout était vert. Rien n'avait été fait.

[relance · PAS · agitation (roadblock_why)]
Vous voyez le problème ? Un agent qui relit son propre travail valide ses propres erreurs.

[PAS · solution + FAB · sens (savoir en 10 minutes ; et alors ? pas besoin de lire le code ; et alors ? vous ne croyez plus sur parole)]
Le Test à l'Aveugle est la checklist et le prompt à copier qui confient la vérification à un second agent, un agent qui n'a rien vu de la construction. Vous savez en 10 minutes si votre agent a vraiment fait ce qu'il annonce.

[liste « taste » (script free : « Here's a taste of what you get »)]
Voici un aperçu de ce que contient Le Test à l'Aveugle :

[FAB · fonction → avantage → bénéfice (et alors ? pas de validation de ses propres erreurs)]
- Le prompt à copier qui transforme un second agent en vérificateur. Il n'a rien vu de la construction, donc il ne valide pas ses propres erreurs.

[FAB · bénéfice]
- Comment écrire ce que « terminé » veut dire avant de lancer l'agent. Vous cessez de croire un « terminé » que personne n'a défini.

[FAB · bénéfice (réponse à la fausse croyance)]
- La checklist pour contrôler le travail de l'agent sans lire une ligne de code. Vous n'avez pas besoin d'apprendre à coder pour savoir si ça marche.

[FAB · sens (ce qui est prouvé, ce qui ne l'est pas)]
- Comment savoir, fonctionnalité par fonctionnalité, ce qui est prouvé et ce qui ne l'est pas.

[relance (bucket brigade)]
Et ce n'est pas tout : vous le recevez par e-mail, et il fonctionne avec Claude Code, Cursor, Codex, Lovable ou Bolt.

Votre adresse e-mail

[appel à l'action · verbe d'abord, avec sa raison (juste dessous)]
[BOUTON] Envoyez-moi le Test à l'Aveugle

Cliquez maintenant : le test arrive dès que vous avez confirmé votre adresse. Un e-mail pour confirmer, puis le test, puis quelques e-mails de WebModerne sur la fiabilité avec les agents de code. Désinscription en un clic.

[preuve : constraints.proof[2] ; aucun témoignage (première cohorte)]
Nous l'utilisons sur notre propre travail. Un premier agent vierge, lancé à l'aveugle sur notre outil copy-funnel, a trouvé les 6 pièges que nous avions cachés dans le brief de test.

[P.S. · rappel de l'offre, limite honnête (la méthode ne supprime pas les bugs), appel à l'action répété avec une raison]
P.S. Le test est gratuit et il dure 10 minutes. Il ne supprime pas les bugs : il vous dit ce qui est prouvé et ce qui ne l'est pas. Envoyez-vous-le avant la prochaine fonctionnalité que votre agent déclare terminée.
```

## 5. Contrôle

| élément | valeur | source |
|---|---|---|
| titre | « Comment savoir si votre agent a vraiment fait ce qu'il annonce… même si vous ne savez pas coder » | `scripts/01-titres.md` §3, mot pour mot |
| pré-titre | « Le Test à l'Aveugle · gratuit · 10 minutes » | `scripts/01-titres.md` §3 |
| « 10 minutes » | durée de la checklist, pas un résultat client | `lead_magnet.promise` |
| « succeeded », code de sortie 0, sans avoir rien fait | citation de la preuve | `constraints.proof[0]` |
| « 6 pièges » | un premier agent vierge sur copy-funnel | `constraints.proof[2]` |
| outils nommés (Claude Code, Cursor, Codex, Lovable, Bolt) | liste des outils compatibles | `benefits[1]` |
| nombre de cases de la checklist | retiré (l'ancienne version annonçait « 7 cases » : chiffre absent du brief) | contrôle « aucune preuve inventée » |
| témoignage | aucun (première cohorte) ; remplacé par la preuve copy-funnel | `constraints.testimonials: []` |

- Citations de la garantie : **0** (page d'inscription : elle n'apparaît pas).
- Formulaire : `action="merci.html" method="get"` conservé ; style en ligne conservé.
- Mots bannis (mots entiers) : voir `fr_check` ci-dessous.

# Partie B · Page de remerciement du double opt-in (merci.html) · who-what-why-how-script-2

## 1. Gabarit (extrait verbatim du corpus, en anglais, avec ses {variables})

```text
Option #2: "Who, What, Why, How" Problem, Agitate, Solve

Have you been {no1pain}?

Do you want to {desire1}, but don't know where to start ?

Then this {targettype} is the answer you've been looking for.

Hi, I'm {yourname}, founder of {yourcompany}.

I've got an amazing {targettype} for you called "{targettitle}."

It makes it easy for you to {no1desire}, so you can {desire1}.

Claim your access now and we'll get you started with the {targettitle} immediately.

Here's exactly what you get:
* {elementtitle} - ({elementvalue} Value)

Total Value: {totalvalue}

Your Price Today: {todayprice}

At this point you might be thinking "This sounds great, but there's gotta be a catch, right ?"

There's no catch !

I'm doing this because {whygivingaway}.

All you need to do is register and you can get started right away (even if it's 2:00 a.m. in the morning!).

Now, this {targettype} offer can't last forever... So don't wait !

And, if for any reason you don't love it, I'll refund your money and you can still keep access to the {targettype} and get value from it in the future.

Here's what you're going to get right now with the "{targettitle}" {targettype}:

Act Now and you get:
* {elementtitle} - ({elementvalue} Value)

Let "{targettitle}" help you {desire1} too !

Just click the button to get started instantly.
```

## 2. Variables remplies

| variable | question du script | valeur en français | champ du brief |
|---|---|---|---|
| `yourname` | Your name | Karnon Koné | `author.name` |
| `yourcompany` | Your company | WebModerne | `author.company` |
| `targettype` | What are you offering to get them to sign up | une cohorte en direct | `offer.type` |
| `targettitle` | Title of your offer | Construire Fiable | `offer.name` |
| `elementtitle` / `elementvalue` | Title / value of this part | (page soft : 3 pièces nommées sans valeurs ; valeurs sur la page de vente) | `offer.stack[*]` |
| `totalvalue` | Total value | 774 € (affiché sur la page de vente et de commande, pas ici) | `offer.total_value` |
| `todayprice` | Price today | 297 € | `offer.price.today` |
| `desire1` | Big payoff (VERB) | savoir à tout moment ce qui est prouvé et ce qui ne l'est pas | `outcome.supporting[1]` (promesse réduite au processus, S8) |
| `no1pain` | Big pain to avoid | croire l'agent sur parole | `pain.top` |
| `no1desire` | Cool discovery they will make | appliquer le test à l'aveugle à chaque fonctionnalité de votre projet | `offer.mechanism`, `offer.what_it_is` |
| `whygivingaway` | Why so inexpensive | prix de la cohorte fondatrice ; il passe à 497 € à la cohorte suivante | `offer.pricedrop_reason` |

## 3. Version remplie brute (gabarit traduit, variables remplacées en **gras**, avant réécriture)

**Avez-vous été croire l'agent sur parole ?** (Option #2 : Problem, Agitate, Solve)

Vous voulez **savoir à tout moment ce qui est prouvé et ce qui ne l'est pas**, mais vous ne savez pas par où commencer ?

Alors cette **cohorte en direct** est la réponse que vous cherchiez.

Bonjour, je suis **Karnon Koné**, fondateur de **WebModerne**.

J'ai une **cohorte en direct** géniale pour vous, appelée « **Construire Fiable** ».

Elle vous permet facilement de **appliquer le test à l'aveugle à chaque fonctionnalité de votre projet**, pour que vous puissiez **savoir à tout moment ce qui est prouvé et ce qui ne l'est pas**.

Voici exactement ce que vous obtenez : * **4 ateliers en direct de 90 minutes** * **4 revues écrites de vos rapports de test** * **Le kit Preuve**

Votre prix aujourd'hui : **297 €**

Vous pensez peut-être : « Il y a forcément un piège ? » Il n'y en a pas. Je fais cela parce que **c'est le prix de la cohorte fondatrice ; il passe à 497 € à la cohorte suivante**.

Cette offre de **cohorte en direct** ne peut pas durer toujours… Alors n'attendez pas !

Laissez « **Construire Fiable** » vous aider à **savoir à tout moment ce qui est prouvé** aussi !

## 4. Version finale (réécrite selon Jim Edwards)

```text
Dernière étape

[titre (étape double opt-in, inchangé)]
Confirmez votre adresse.

[consigne unique : confirmer]
Ouvrez l'e-mail que nous venons d'envoyer et cliquez sur le lien. Le Test à l'Aveugle arrive juste après. Si vous ne voyez pas l'e-mail, regardez dans vos courriers indésirables.

[PAS · problème (question) · accroche : Question]
Votre agent vous a-t-il déjà dit « c'est fait » sur quelque chose qui ne l'était pas ? Le test vous aide à le voir. Pendant qu'il arrive, un mot sur la suite.

[Who (qui)]
Qui : Karnon Koné, co-fondateur de WebModerne. Nous faisons tourner notre propre activité avec des agents IA, et nous vérifions tout ce qu'ils produisent.

[What · FAB : fonction (3 pièces, 3 bonus sans valeurs ici : la page de vente les détaille)]
Quoi : une cohorte de 4 semaines en direct, Construire Fiable, pour appliquer le test à l'aveugle à votre propre projet. Vous y trouvez 4 ateliers en direct de 90 minutes, 4 revues écrites de vos rapports de test et le kit Preuve, plus trois bonus.

[Why · PAS · solution + FAB · sens (ce qui est prouvé, ce qui ne l'est pas)]
Pourquoi : le test que vous allez recevoir vous dit si l'agent a menti sur une chose. La cohorte vous apprend à appliquer ce test à chaque fonctionnalité de votre projet, pour que vous sachiez à tout moment ce qui est prouvé et ce qui ne l'est pas.

[How · prix, places, dates, clôture, raison du prix (épine v2)]
Comment : 30 places (nous relisons chaque rapport de test à la main), les lundis 16, 23, 30 novembre et 7 décembre 2026 à 19h00 (heure de Paris), en visio. Prix de la cohorte fondatrice : 297 €, il passe à 497 € à la cohorte suivante. Inscriptions fermées le vendredi 13 novembre 2026 à 23h59 (heure de Paris).

[preuve honnête à la place du témoignage (constraints.proof[4])]
C'est la première cohorte : nous n'avons aucun témoignage à vous montrer, et nous ne vous en inventerons pas. Ce que nous avons : l'outil copy-funnel est passé par 3 tours de test à l'aveugle avant d'être livré.

[appel à l'action doux · verbe d'abord]
Les détails sont ici, sans engagement : Voir Construire Fiable

[appel à l'action principal : le test d'abord]
Commencez par le test. C'est lui qui compte aujourd'hui.

[P.S. · priorité au test]
P.S. Lisez le test d'abord, la page de la cohorte ensuite. Si le test vous suffit, nous sommes contents aussi.

Démo de revue : voir directement le Test à l'Aveugle (ce que reçoit l'abonné après confirmation).
```

## 5. Contrôle

| élément | valeur | source |
|---|---|---|
| cohorte de 4 semaines, 30 places, dates | lundis 16, 23, 30 novembre et 7 décembre 2026, 19h00 (heure de Paris) | épine v2 ; `event.*` |
| 297 € / 497 € | prix aujourd'hui / à la cohorte suivante | épine v2 ; `offer.price.*` |
| clôture | vendredi 13 novembre 2026 à 23h59 (heure de Paris) | `offer.deadline` |
| « 4 ateliers de 90 minutes », « 4 revues écrites », « kit Preuve », « trois bonus » | composition de l'offre ; valeurs non affichées sur cette page (le gabarit les liste, la page soft les renvoie à la page de vente) | `offer.stack`, `offer.bonuses` |
| « 3 tours de test à l'aveugle » | outil copy-funnel avant livraison | `constraints.proof[4]` |
| témoignage | aucun, dit explicitement (« nous n'avons aucun témoignage à vous montrer ») | `constraints.testimonials: []` |

- Citations de la garantie : **0** (non reprise sur la page soft ; elle figure sur la page de commande).
- Style : `style.css` lié, note « Démo de revue » conservée, lien `test-aveugle-kit.html` et `index.html` conservés.
- Mots bannis : voir `fr_check`.

# Partie C · Page de commande avec order bump (commande.html) · order-bump-script-2

## 1. Gabarit (extrait verbatim du corpus, en anglais, avec ses {variables})

```text
Final Step: Browse through the results and watch the idea sparks start to fly !
(We apologize in advance if you get TOO MANY awesome ideas!)

Variables Entered

What is the name of what you're offering in the bump ? {targettitle}
What are you offering for the bump ? {targettype}
What's the big no1desire of what you're offering?(VERB) {no1desire}
What simple action do they need to take to get the no1desire ? {act}
What's a no1pain thing or action they want to avoid ? "...without _____ !" {no1pain}
How much is the what you're offering (todayprice) ? {todayprice}

Instructions:

Step 1: Choose a Check Box Copy
Step 2: Choose a Quick Offer Copy
Step 3: Choose a Blurb
Step 4: Choose an Order Button Copy
Step 5: Use to build your Order Bump offer




Step #1: CHECK BOX COPY

Yes, I will Take It !

Yes, I Want It !

Yes, I Want It Now !

Yes ! I Want This

Yes ! I Want the {targettype}

Yes ! Give Me the {targettype} Too !

Yes ! Give Me the {targettitle} Too !

Yes, I would like free shipping

Yes, I Want the {targettitle} Too !

Yes, I Want the {targettitle} for Only {todayprice}

Yes, Add {targettype} for only {todayprice}

Yes ! I Want To Upgrade to the {targettype}

Yes ! I Want To Upgrade to {targettitle}


Step #2: QUICK OFFER COPY

ONE TIME OFFER (Just {todayprice}):

ONE TIME OFFER - Only {todayprice}:

ONE TIME OFFER:

THE POSTAGE IS ALREADY PAID !


Step #3: BLURB

Add {targettype} so you can {no1desire}! Click YES to add this to your order now for just {todayprice}! (This offer is not available at ANY other time or place)

Want our {targettitle}? It's proven to {no1desire}! Click YES to add this to your order now for just {todayprice}! (This offer is not available at ANY other time or place)

Want our {targettitle}? It's proven to {no1desire} without {no1pain}! Click YES to add this to your order now for just {todayprice}! (This offer is not available at ANY other time or place)

Want the new {targettype} version of {targettitle} that helps you {no1desire}? *** Click YES to add this to your order now for just a single payment of {todayprice}! (This offer is not available at ANY other time or place)

Want the new {targettitle} that helps you {no1desire}? *** Click YES to add this to your order now for just a single payment of {todayprice}! (This offer is not available at ANY other time or place)

Want the {targettype} we use to {no1desire}? It's proven to work and all you have to do is {act} and you'll be ready to {no1desire}! Click YES to add this to your order now for just {todayprice}! (This offer is not available at ANY other time or place)

Want the {targettype} we use to get results fast ? All you have to do is {act} and you'll {no1desire}! Click YES to add this to your order now for just {todayprice}! (This offer is not available at ANY other time or place)

Add a / an / the {targettype} for only {todayprice} and get FREE SHIPPING on the entire order. That's a savings of XX. Offer only valid with this order.

For a limited time get the complete {targettitle} for XX% off ! This {targettype} helps you {no1desire} without {no1pain}. Get yours today !

You'd be crazy not to add the {targettype} for only {todayprice}! We'll send it along with your order so you can {no1desire} (without {no1pain}).

Want our NEW "{targettitle}" that helps you {no1desire} without {no1pain}?*** Click YES to add this to your order now for just a single payment of {todayprice}! (This offer is not available at ANY other time or place)

Want our NEW {targettype} "{targettitle}" that helps you {no1desire} without {no1pain}?*** Click YES to add this to your order now for just a single payment of {todayprice}! (This offer is not available at ANY other time or place)

You can {no1desire} and we'll do all the work for you ! Just add this one time special offer to upgrade your purchase with our {targettitle}.


Step #4: ORDER BUTTON COPY

Complete Order

Ship My {targettype} Now !

Complete Your Order Now
```

## 2. Variables remplies

| variable | question du script | valeur en français | champ du brief |
|---|---|---|---|
| `targettitle` | Name of the bump | Les replays à vie | `offer.bump.name` |
| `targettype` | What are you offering for the bump | accès à vie aux replays des 4 ateliers et de l'atelier bonus, au lieu de 12 mois | `offer.bump.what_it_is` |
| `no1desire` | Big payoff (VERB) | revoir un atelier le jour où vous attaquez une nouvelle fonctionnalité, même dans deux ans | `offer.bump.benefit` |
| `act` | Simple action (VERB) | cocher la case | — (action du formulaire) |
| `no1pain` | Thing they want to avoid | perdre l'accès aux replays au bout de 12 mois | `offer.access` (replays 12 mois) |
| `todayprice` | Price of the bump | 27 € | `offer.bump.price` |
| (résumé d'offre) | — (pas un script ; empilement de valeur de l'épine v2) | 3 pièces, 3 bonus avec valeurs, 774 €, 297 €, garantie | `offer.stack`, `offer.bonuses`, `offer.total_value`, `offer.guarantee` |

## 3. Version remplie brute (gabarit traduit, variables remplacées en **gras**, avant réécriture)

Offre à cocher : **Les replays à vie**

**OFFRE UNIQUE (seulement 27 €) :**

[Case] **Oui, ajoutez** **accès à vie aux replays des 4 ateliers et de l'atelier bonus, au lieu de 12 mois** **pour seulement 27 €**

Blurb : Voulez-vous **Les replays à vie** ? Cliquez OUI pour l'ajouter à votre commande maintenant pour seulement **27 €** ! Vous pouvez **revoir un atelier le jour où vous attaquez une nouvelle fonctionnalité, même dans deux ans**, sans **perdre l'accès au bout de 12 mois**.

Bouton : **Valider ma commande**

## 4. Version finale (réécrite selon Jim Edwards)

```text
Commande

[titre de page de commande]
Construire Fiable · cohorte fondatrice

[rappel (témoin réutilisé, 01-titres.md §3)]
Votre agent dit « terminé ». Prouvez-le, fonctionnalité par fonctionnalité, sur votre propre projet.

[empilement de valeur]
Voici tout ce que vous recevez

[3 pièces]
Les 3 pièces de la cohorte

[FAB · et alors ? appliquer sur son projet ; et alors ? preuves au lieu de promesses]
- 4 ateliers en direct de 90 minutes (388 €) : à chaque séance, vous passez une fonctionnalité de votre projet au test à l'aveugle. Vous appliquez la méthode sur votre application, pas sur un exemple. À la fin, votre projet a des preuves au lieu de promesses.

[FAB · et alors ? savoir quoi corriger ; et alors ? plus seul devant « l'appli ne marche pas »]
- 4 revues écrites de vos rapports de test (188 €) : chaque semaine, nous relisons le rapport du second agent sur votre projet. Vous savez quoi corriger en premier. Vous ne restez plus seul devant « l'appli ne marche pas ».

[FAB · et alors ? mêmes garde-fous ; et alors ? la méthode reste]
- Le kit Preuve (47 €) : le cahier « terminé veut dire », le prompt du test à l'aveugle et la checklist avant publication. Vous gardez les mêmes garde-fous à chaque nouvelle fonctionnalité. La méthode reste quand la cohorte est finie.

[relance + 3 bonus]
Et ce n'est pas tout : 3 bonus

[FAB · bonus 1]
- Le pack 30 prompts de vérification (27 €) : 30 prompts prêts à coller pour tester une connexion, un paiement, un formulaire, un import de données. Vous ne vous demandez plus quoi tester.

[FAB · bonus 2]
- Le guide « Brancher le second agent » (27 €) : comment lancer le second agent avec Claude Code, Cursor, Codex, Lovable et Bolt. Vous n'avez pas à changer d'outil.

[FAB · bonus 3]
- L'atelier bonus de questions-réponses du lundi 14 décembre 2026 (97 €) : 90 minutes, une semaine après la dernière séance, pour les blocages rencontrés seul. Vous n'êtes pas lâché à la fin des 4 semaines.

[extra offert sans valeur (brief offer.extras)]
Offert, sans valeur affichée (il n'est pas vendu seul) : le groupe Facebook privé des bâtisseurs fiables.

[valeur totale + base des valeurs]
Valeur totale : 774 € (388 + 188 + 47 + 27 + 27 + 97). Base des valeurs : le prix de chaque élément vendu seul chez WebModerne (à mettre en vente avant le lancement).

[prix + raison du prix]
Votre prix aujourd'hui : 297 €, au lieu de 497 €. C'est le prix de la cohorte fondatrice : il passe à 497 € à la cohorte suivante.

[dates, clôture, places]
Séances en direct les lundis 16, 23, 30 novembre et 7 décembre 2026 à 19h00 (heure de Paris), en visio. Inscriptions fermées le vendredi 13 novembre 2026 à 23h59 (heure de Paris). 30 places, parce que nous relisons chaque rapport de test à la main.

[order bump · case à cocher (script : « Yes, Add {targettype} for only {todayprice} » ; ici avec le blurb)]
Oui, ajoutez Les replays à vie (27 €).

Accès à vie aux replays des 4 ateliers et de l'atelier bonus, au lieu de 12 mois. Vous revoyez un atelier le jour où vous attaquez une nouvelle fonctionnalité, même dans deux ans. La méthode reste à portée de main tant que votre projet vit.

[garantie (1re et seule citation de la page)]
La Garantie Preuve

[garantie mot pour mot]
Notre engagement : si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles.

[bouton de commande · verbe d'abord (script : « Complete Order »)]
[BOUTON] Valider ma commande (297 €)

[raison de l'appel à l'action + total avec et sans bump]
Cliquez maintenant pour réserver l'une des 30 places avant la clôture. Total : 297 €, ou 324 € si vous cochez Les replays à vie (27 €).

[accès]
Accès immédiat aux modèles après paiement ; première séance en direct le lundi 16 novembre 2026 ; replays disponibles 12 mois.

[P.S. · preuve honnête (constraints.proof[2]) à la place du témoignage]
P.S. C'est la première cohorte : nous n'avons aucun témoignage à vous montrer. Nous avons la preuve de notre propre travail : un premier agent vierge, lancé à l'aveugle sur notre outil copy-funnel, a trouvé les 6 pièges que nous avions cachés dans le brief de test. Et la Garantie Preuve ci-dessus protège votre commande.
```

## 5. Contrôle

| élément | valeur | source |
|---|---|---|
| 388 € | 4 × 97 € (4 ateliers en direct de 90 minutes) | `offer.stack[0]` |
| 188 € | 4 × 47 € (4 revues écrites) | `offer.stack[1]` |
| 47 € | le kit Preuve | `offer.stack[2]` |
| 27 € / 27 € / 97 € | pack 30 prompts / guide « Brancher le second agent » / atelier bonus du 14 décembre 2026 | `offer.bonuses[*]` |
| **774 €** | 388 + 188 + 47 + 27 + 27 + 97 = 774 | épine v2 ; `offer.total_value` |
| base des valeurs | prix de chaque élément vendu seul chez WebModerne (à mettre en vente avant le lancement) | épine v2 |
| groupe Facebook | offert, sans valeur affichée | `offer.extras` |
| 297 € / 497 € | prix aujourd'hui / ensuite (raison : prix de la cohorte fondatrice) | `offer.price.*` |
| bump 27 € ; 324 € avec bump | 297 + 27 = 324 | `offer.bump.price` |
| 30 places, dates, clôture 13 novembre 23h59 | | `event.capacity`, `event.date`, `offer.deadline` |
| « 6 pièges » (P.S.) | copy-funnel | `constraints.proof[2]` |
| témoignage | aucun (P.S. le dit) | `constraints.testimonials: []` |

- Citations de la garantie : **1**, mot pour mot : « si au 30e jour après la première séance vous n'avez pas une fonctionnalité de votre projet qui passe son test à l'aveugle, écrivez-nous et nous vous remboursons intégralement. Vous gardez les modèles. » (introduite par « Notre engagement : », la phrase commence en minuscule pour rester verbatim).
- Le pack 30 prompts, ancien bump, est désormais un bonus (épine v2) ; le bump est Les replays à vie.
- Formulaire : `action="merci-achat.html" method="get"`, case `name="bump"`, note « Démo de revue » conservée.
- Mots bannis : voir `fr_check`.

# Partie D · OTO après achat (merci-achat.html) · oto-done-with-you

## 1. Gabarit (extrait verbatim du corpus, en anglais, avec ses {variables})

```text
-------------------------
Confirm Decision
-------------------------

Hey, it's {yourname} here again.

I want to congratulate you for claiming your access to the "{namewhatjustbought}" {whatitis2}.

-------------------------
Smart / Why ?
-------------------------

You made a really smart decision, and here’s why…

You ordered "{namewhatjustbought}" because you want to {no1desireprevious}, and that’s exactly what it’s going to do for you.

This {whatitis2} you just bought access to is the entire framework I personally use to {no1desireprevious} myself.

-------------------------
Question
-------------------------

But let me ask you a question...

How would you like to take your {kwfocus1} to the next level ?

-------------------------
Next / More
-------------------------

The great news is, "{namewhatjustbought}" is kinda like me handing you the blueprints for your dream mansion. Now that you have access to the {kwfocus1} {whatitis2}, you now have the complete set of blueprints for the house. And what I want to offer you next is basically the entire training on how to build the actualhouse step by step so you can live happily ever after.

It’s called the {targettitle}.

This step-by-step {targettype} is going to teach you my exact frameworks to {no1desire} on a really deep, detailed, granular level.

-------------------------
Exclusive
-------------------------

And we're only making it available to you right now because you proved you're an action taker when you took advantage of the "{namewhatjustbought}" {whatitis2} offer.

-------------------------
Results Fast / Speed
-------------------------

The {targettitle} explains the entire {kwfocus1} framework using in-depth videos and more in so much detail it’s literally like me doing it with you as you watch over my shoulder.

In fact, the training in this {targettype} is so detailed you could even hand it off to a member of your team or someone else and have them do everything for you.

-------------------------
The 1 Thing
-------------------------

I don't have time to go over everything inside of the {targettitle} because we could be here for hours.

But I will tell you, other than hiring me to do it for you, watching over my shoulder in this {targettype} is your FASTEST, easiest, most direct path to {no1desire} in {timeframe}.

If you ultimately want to {bottomline1}, this is the in depth training and tools you want !

-------------------------
Future Casting
-------------------------

Just imagine what your life will be like when you have the ability to {no1desire}... any time you want !

How much faster could you reach your {kwfocus1} goals ?

How much better would your life be ?

-------------------------
CTA
-------------------------

So click the button below right now to add the {targettitle} to your order.

-------------------------
Guarantee
-------------------------

I guarantee it will help you to {no1desire} in {timeframe} or I'll cheerfully refund your money, no questions asked.

-------------------------
Value Stacking
-------------------------

Act now and here's exactly what you get:

{elementtitle} ({elementvalue} Value)
This {whatitis} makes it easy to {feature}, {featurebenefit}, and {meaning}.


{targettitle} has a total value of {totalvalue}

In fact, {targettitle} is available on my website for {regprice}.

-------------------------
Scarcity
-------------------------

But right now, you have this ONE CHANCE to get it for only {todayprice}.

This one-time offer is only available right here, right now. When you leave this page, it's gone forever.

-------------------------
CTA
-------------------------

Don't miss your chance to watch over my shoulder step by step so you can {no1desire} faster and easier than ever.

Click the button now.

-------------------------
OPTIONAL Section: Testimonial Rush at End
-------------------------

Don't just take my word for it, take a look at what others are saying about {targettitle}. . .

"Optional but highly recommended"

"Optional but highly recommended"

"Optional but highly recommended"

-------------------------
CTA
-------------------------

Go ahead, grab your access to {targettitle} and I’ll see you on the inside !
```

## 2. Variables remplies

| variable | question du script | valeur en français | champ du brief |
|---|---|---|---|
| `yourname` | Your name | Karnon Koné (« nous » dans le texte) | `author.name` |
| `kwfocus1` | #1 area of focus | agent de code, logiciel fiable | `topic.focus` |
| `bottomline1` | #1 thing they want to do | savoir à tout moment ce qui est prouvé et ce qui ne l'est pas dans votre projet | `outcome.supporting[1]` |
| `namewhatjustbought` | What they just bought | Construire Fiable | `offer.name` |
| `whatitis2` | The thing they just bought | cohorte en direct | `offer.type` |
| `no1desireprevious` | Result from the previous offer (VERB) | appliquer le test à l'aveugle à votre propre projet | `offer.what_it_is` |
| `targettitle` | Name of the OTO | La Revue Preuve en duo | `offer.upsell.name` |
| `targettype` | What exactly is sold | accompagnement : deux visios de 45 minutes | `offer.upsell.type`, `what_it_is` |
| `no1desire` | Result from the OTO (VERB) | obtenir un diagnostic de votre application fait à deux, avec la liste priorisée de ce qui n'est pas prouvé | `offer.upsell.result` |
| `elementtitle`, `whatitis`, `feature`, `featurebenefit`, `meaning` | Value stack, un seul élément | La Revue Preuve en duo ; deux visios ; passer votre projet au test à l'aveugle avec vous ; voir en direct ce qui n'est pas prouvé ; ne plus deviner par où commencer | `offer.upsell.*` |
| `elementvalue`, `totalvalue`, `regprice` | values / regular price | NON REMPLIES : aucun prix barré (spine v2) | — |
| `todayprice` | Price today | 197 € | `offer.upsell.price.today` |
| `timeframe` | Timeframe | NON REMPLIE : aucun délai promis ; garantie du gabarit supprimée (S6) | — |

## 3. Version remplie brute (gabarit traduit, variables remplacées en **gras**, avant réécriture)

Confirmer la décision : **Karnon**, de nouveau. Je vous félicite d'avoir réservé votre place dans « **Construire Fiable** », **cohorte en direct**.

Vous avez pris une décision intelligente, et voici pourquoi : vous avez commandé « **Construire Fiable** » parce que vous voulez **appliquer le test à l'aveugle à votre propre projet**.

Mais laissez-moi vous poser une question : comment aimeriez-vous faire passer votre **agent de code** au niveau supérieur ?

La bonne nouvelle : ce que je vous propose ensuite s'appelle **La Revue Preuve en duo**. Cet **accompagnement** va vous aider à **obtenir un diagnostic de votre application fait à deux, avec la liste priorisée de ce qui n'est pas prouvé**.

Exclusif : proposé seulement maintenant, parce que vous avez agi en commandant « **Construire Fiable** ».

**La Revue Preuve en duo** : cet **accompagnement** vous permet de **passer votre projet au test à l'aveugle avec nous**, **voir en direct ce qui n'est pas prouvé**, et **ne plus deviner par où commencer**.

Je n'ai pas le temps de tout détailler ici.

Appel à l'action : cliquez sur le bouton ci-dessous pour ajouter **La Revue Preuve en duo** à votre commande.

[Garantie du gabarit : supprimée, aucune garantie annoncée pour l'OTO.]
[Value stacking : valeur et prix barré supprimés.]

Mais maintenant, vous avez cette UNE chance de l'obtenir pour seulement **197 €**.

Cette offre unique n'est disponible qu'ici et maintenant. Quand vous quittez cette page, elle disparaît.

Appel à l'action : ne manquez pas votre chance. Cliquez maintenant.

[Témoignages : aucun (première cohorte).]

## 4. Version finale (réécrite selon Jim Edwards)

```text
Commande confirmée

[titre (confirmation, inchangé)]
C'est fait. Votre place dans Construire Fiable est réservée.

[Confirm Decision + Smart / Why (sans re-vendre la cohorte)]
Félicitations : vous venez de rejoindre la cohorte fondatrice. Vous avez pris une bonne décision : vous voulez des preuves au lieu de promesses. Le kit Preuve arrive dans votre boîte mail, et nous nous retrouvons le lundi 16 novembre 2026 à 19h00.

[Question · accroche : Question · PAS · problème]
Une question avant de fermer cette page. Quand le rapport d'une revue vous dit « ceci n'est pas prouvé », savez-vous par où commencer sur votre application ?

[PAS · agitation : l'écart honnête, l'attention individuelle que le groupe ne donne pas ; relance « Vous voyez le problème ? »]
Une précision honnête sur ce que la cohorte fait et ne fait pas. Les séances sont en groupe, et la revue hebdomadaire est écrite. Si votre projet a besoin d'un tête-à-tête, où une personne regarde votre application tourner avec vous et vous seul, la cohorte ne le prévoit pas. Vous voyez le problème ?

[Next / More · nom de l'offre]
La Revue Preuve en duo

[FAB · fonction → avantage → bénéfice → sens (et alors ? vous voyez en direct ; et alors ? diagnostic à deux ; et alors ? vous ne devinez plus par où commencer)]
Deux visios de 45 minutes où nous passons votre projet au test à l'aveugle avec vous. Vous voyez, en direct, ce qui n'est pas prouvé dans votre application. Vous repartez avec un diagnostic fait à deux, et la liste priorisée de ce qui n'est pas prouvé. Vous ne devinez plus par où commencer.

[limite honnête, aucune promesse de résultat, aucune garantie annoncée]
Ce que cela n'est pas : une promesse de résultat. C'est deux séances de 45 minutes, sur votre projet, avec nous.

[prix unique 197 €, sans prix barré]
Elle n'est proposée que sur cette page : 197 €.

[appel à l'action 1 · verbe d'abord]
[BOUTON] Oui, j'ajoute la Revue Preuve en duo (197 €)

[LIEN] Non merci, je garde la cohorte seule

[Scarcity (script : « When you leave this page, it's gone ») + raison de l'appel à l'action]
Cette offre n'existe qu'ici : quand vous quittez cette page, elle disparaît. Ajoutez-la maintenant, et nous vous écrivons ensuite pour convenir des deux visios avec vous.

[appel à l'action 2 (répété, avec sa raison juste au-dessus)]
[BOUTON] Ajoutez la Revue Preuve en duo à ma commande (197 €)

[P.S. · sortie honnête]
P.S. Si la cohorte seule vous suffit, cliquez sur « Non merci ». Votre place reste réservée.

Démo de revue : les boutons ne débitent rien.
```

## 5. Contrôle

| élément | valeur | source |
|---|---|---|
| 197 € | prix unique de l'OTO, aucun prix barré, aucune valeur | épine v2 ; `offer.upsell.price.today` |
| 2 visios de 45 minutes | contenu de l'OTO | `offer.upsell.what_it_is` |
| 16 novembre 2026 à 19h00 | première séance (rappel) | `offer.access` ; `event.*` |
| dates de l'OTO | aucune créée (« nous vous écrivons pour convenir des deux visios ») | contrôle « aucune autre date » |
| témoignage, preuve chiffrée | aucun ; aucune promesse de résultat (« Ce que cela n'est pas : une promesse de résultat ») | `constraints.claims_policy` |

- Citations de la garantie : **0** (aucune garantie sur l'OTO ; la cohorte n'est pas revendue).
- Cohorte non re-vendue ; l'écart est l'attention individuelle que la cohorte en groupe ne donne pas (texte honnête conservé de la version précédente).
- Boutons : `href="#"` conservés ; la note « Démo de revue » devient « les boutons ne débitent rien » (il y a maintenant deux boutons d'ajout, plus le lien « Non merci »).
- Mots bannis : voir `fr_check`.
