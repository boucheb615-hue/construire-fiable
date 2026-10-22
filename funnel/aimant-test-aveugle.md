# Le Test à l'Aveugle

**Savoir en 10 minutes si votre agent a vraiment fait ce qu'il annonce.**
Une checklist et un prompt à copier. Aucune ligne de code à lire.
WebModerne

---

## Avant de commencer (2 minutes)

Choisissez **une seule** chose que l'agent dit avoir faite. Exemple : « le formulaire de contact envoie maintenant un e-mail ».

Écrivez en dessous, en phrases simples, ce que « terminé » veut dire. Trois lignes suffisent :

1. Ce que je fais : « je remplis le formulaire avec mon adresse et je clique sur Envoyer ».
2. Ce que je dois voir : « un message de confirmation à l'écran ».
3. Ce qui doit se passer ailleurs : « je reçois l'e-mail dans les 2 minutes ».

Ajoutez **un cas qui doit échouer** : « si je laisse l'adresse vide, je vois une erreur et rien n'est envoyé ». C'est là qu'un agent peut tricher sans que vous le voyiez.

## La checklist (5 minutes)

Cochez seulement ce que vous avez **vu vous-même** ou ce que le second agent a **prouvé**. « L'agent me l'a dit » ne compte pas.

- [ ] J'ai écrit les critères **avant** de relire ce que l'agent a fait.
- [ ] Le second agent n'a **pas** vu la conversation avec le premier.
- [ ] Chaque critère a un résultat : prouvé ou pas prouvé.
- [ ] Le cas qui doit échouer a été testé, pas seulement le cas qui marche.
- [ ] Ce qui marchait **avant** la correction marche encore.
- [ ] Le rapport dit **comment** chaque critère a été vérifié (pas seulement « OK »).
- [ ] Rien n'est marqué « probablement », « devrait » ou « en théorie ».

Une case vide = pas terminé. Même si l'écran est vert.

## Le prompt du second agent (3 minutes)

Ouvrez une **nouvelle** conversation, avec un agent qui n'a rien vu de la construction (Claude, ChatGPT ou celui de votre éditeur). Collez :

```
Tu es un vérificateur. Tu n'as pas construit cette application et tu ne
fais pas confiance à ce qui t'a été dit sur elle.

Voici l'application : [lien, ou accès au dossier du projet]
Voici les critères de « terminé », écrits avant la construction :
[collez vos 3 lignes + le cas qui doit échouer]

Pour CHAQUE critère :
1. Dis comment tu le vérifies concrètement (ce que tu cliques, ce que tu
   lances, ce que tu lis).
2. Fais-le vraiment.
3. Donne le verdict : PROUVÉ ou PAS PROUVÉ, avec ce que tu as observé.

Règles :
- « Le code a l'air correct » n'est pas une preuve.
- Si tu ne peux pas vérifier un critère, écris PAS PROUVÉ et explique
  ce qui te manque. N'invente pas.
- Termine par la liste des critères PAS PROUVÉS, dans l'ordre où je dois
  les corriger.
```

Ensuite, renvoyez la liste des critères **PAS PROUVÉS** au premier agent. Puis relancez le second, dans une nouvelle conversation encore. Vous avez terminé quand tout est PROUVÉ.

---

**Et après ?** Ce test vous dit si l'agent a menti sur une chose. Construire Fiable vous apprend à appliquer ce test à chaque fonctionnalité de votre projet : une cohorte de 4 semaines en direct, 30 places, début le lundi 16 novembre 2026. https://boucheb615-hue.github.io/construire-fiable/
