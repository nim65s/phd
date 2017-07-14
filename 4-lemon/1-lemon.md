## Robots mobiles à tourelle {#sec:lemon}

Dans ce chapitre, nous faisons le rapport d’un projet de robotique réalisé lors de cette thèse en coopération avec
BA Robotic Systems dans le cadre d’un projet avec Metrolab.

### Introduction du projet LEMON

Le projet LEMON, bien plus prosaïque que les autres projets de cette partie, porte sur la conception d’un robot qui
remplacerait une autolaveuse autoportée et son opérateur, dans des endroits tels qu’une station de métro ou un hôpital.

Le prototype d’un tel robot a été réalisé par la société BA Robotic Systems ([@fig:lemon]), et un accord a été conclu
avec le LAAS-CNRS pour que nous concevions l’algorithme de planification de trajectoire.

<div id="fig:lemon">
![](imgs/lemon-1.png){width=40%}
![](imgs/lemon-2.png){width=40%}

Illustrations du prototype du robot LEMON
</div>

Ce projet a été réalisé au sein de la plateforme logicielle libre HPP[^7], développée au sein de l’équipe Gepetto
[@hpp].

[^7]: Humanoid Path Planner

Dans la suite de ce chapitre, nous verrons en premier lieu de quelle manière nous cartographions une zone afin de
faciliter la planification de trajectoire dans la [@sec:carto].

Le robot doit ensuite utiliser une brosse latérale rétractable afin de nettoyer les bords des murs, ce qui est détaillé
dans la [@sec:bordures]. Après cela, le robot doit nettoyer les aires libres d’obstacles grâce à sa brosse principale,
comme nous le verrons dans la [@sec:surfaces].

Enfin, nous expliquerons comment nous relions au mieux toutes ces portions de trajectoires dans la
[@sec:trajectoirefinale], puis quelles optimisations nous avons ajoutées dans la [@sec:optimisation].

Pour conclure, nous exposerons nos résultats et leurs limitations dans la [@sec:lemonres] et les perspectives dans la
[@sec:lemonfutur].
