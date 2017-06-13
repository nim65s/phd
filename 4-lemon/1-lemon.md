## Robots mobiles à tourelle {#sec:lemon}
Les applications possibles de la robotique sont innombrables. Aujourd’hui, bon nombre d’entre elles n’attendent plus
que du temps de travail de roboticiens avant de pouvoir arriver dans nos quotidiens, et faire évoluer la société.

Cependant, cette évolution nécessite une réflexion. Comme le disais Rabelais :

> Science sans conscience n’est que ruine de l’âme.
> \par\raggedleft---  *Pantagruel*, 1542

Il appartient donc au scientifique de réfléchir avant d’agir.

Dans les autres chapitres de cette thèse, nous parlons d’œuvres artistiques et de science fondamentale, mais dans
celui-ci nous verrons une application de la robotique consistant à automatiser une tâche habituellement effectuée par
des êtres humains contre une rémunération.

Au XV^ème^ siècle, quand Gutenberg invente l’imprimerie, les moines copistes perdent leur source de revenu, et sont
remplacés par des ouvriers s’occupants de presses. Les bénéfices pour l’humanité dans les décennies et siècles à
venir sont évidents.

Mais à plus court terme et à plus petite échelle, remplacer un être humain par une machine n’est pas une mince affaire.

On ne veut pas voir des enfants travailler dans des usines de chaussures, mais on ne veut pas non plus qu’ils meurent
de faim faute de revenus.

Pour l’instant, nous n’avons pas de solution miracle. Refuser la robotisation au profit des emplois déjà existants ne
fonctionne pas, comme le montre le retard industriel que la France a pris sur l’Allemagne. Il faut donc accompagner
humainement au mieux les changements apportés par ces nouvelles machines, voire repenser plus globalement la manière
dont sont distribuées les richesses.

### Introduction du projet LEMON

Le projet LEMON, bien plus prosaïque que les autres projets de cette partie, porte sur la conception d’un robot qui
remplacerait une autolaveuse autoportée et son opérateur, dans des endroits tels qu’une station de métro ou un hôpital.

Le prototype d’un tel robot a été réalisé par la société BA Systèmes, et un accord a été conclu avec le LAAS-CNRS pour
que nous concevions l’algorithme de planification de trajectoire.

Ce projet a grandement bénéficié de l’expertise de Florent Lamiraux en planification de trajectoires pour la robotique
mobile, ainsi que de la trousse de développement logiciel HPP[^5], développée au sein de l’équipe Gepetto.

[^5]: Humanoid Path Planner

Dans la suite de ce chapitre, nous verrons en premier lieu comment nous cartographions une zone afin de faciliter la
planification de trajectoire dans la [@sec:carto].

Le robot doit ensuite utiliser une brosse latérale rétractable afin de nettoyer les bords des murs, ce qui est détaillé
dans la [@sec:bordures].  Enfin, le robot doit nettoyer les aires libres d’obstacles grâce à sa brosse principale,
comme nous le verrons dans la [@sec:surfaces].

Pour conclure, nous exposerons nos résultats et leurs limitations dans la [@sec:lemonres] et les perspectives dans la
[@sec:lemonfutur].
