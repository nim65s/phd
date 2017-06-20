## Robots mobiles à tourelle {#sec:lemon}

Dans ce chapitre, nous faisons le rapport d’un projet de robotique réalisé lors de cette thèse en coopération avec
l’entreprise BA Systèmes.

### Introduction du projet LEMON

Le projet LEMON, bien plus prosaïque que les autres projets de cette partie, porte sur la conception d’un robot qui
remplacerait une autolaveuse autoportée et son opérateur, dans des endroits tels qu’une station de métro ou un hôpital.

Le prototype d’un tel robot a été réalisé par la société BA Systèmes, et un accord a été conclu avec le LAAS-CNRS pour
que nous concevions l’algorithme de planification de trajectoire.

Ce projet a grandement bénéficié de l’expertise de Florent Lamiraux en planification de trajectoires pour la robotique
mobile, ainsi que de la trousse de développement logiciel HPP[^7], développée au sein de l’équipe Gepetto [@hpp].

[^7]: Humanoid Path Planner

Dans la suite de ce chapitre, nous verrons en premier lieu comment nous cartographions une zone afin de faciliter la
planification de trajectoire dans la [@sec:carto].

Le robot doit ensuite utiliser une brosse latérale rétractable afin de nettoyer les bords des murs, ce qui est détaillé
dans la [@sec:bordures].  Enfin, le robot doit nettoyer les aires libres d’obstacles grâce à sa brosse principale,
comme nous le verrons dans la [@sec:surfaces].

Pour conclure, nous exposerons nos résultats et leurs limitations dans la [@sec:lemonres] et les perspectives dans la
[@sec:lemonfutur].
