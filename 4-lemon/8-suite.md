### Travaux futurs {#sec:lemonfutur}

Lors de ce projet LEMON réalisé en coopération avec BA Robotic Systems, nous avons tenté de répondre à un cahier des
charges dans un temps limité par le client final. Nous avons donc livré un logiciel fonctionnel, mais sous-optimal.

Dans cette section, nous discutons des possibilités d’extension de ce travail afin de rendre les trajectoires générées
plus proches de celles qui seraient réalisées par un être humain, voire meilleures.

#### Suivi des murs

Dans un premier temps, nous avons choisi de détecter des primitives géométriques afin de suivre les bordures.

<!--TODO: gradient / KHT https://en.wikipedia.org/wiki/Hough_transform#Using_the_gradient_direction_to_reduce_the_number_of_votes-->

Une autre approche possible consisterait à extraire une trajectoire directement de la forme des contours formés par les
`Pixels` de type `BOUNDARY`, en les reliant avec une trajectoire de Dubins. Certains `Pixels` ne seraient pas
atteignables, mais comme nous l’avons vu dans la [@sec:optimisation], ce n’est finalement pas un problème.

Pour cela, l’idéal serait de pouvoir profiter du débattement de la brosse latérale pour mieux gérer la distance entre
le robot et le mur, alors que jusqu’ici nous n’avons considéré qu’elle n’avait que deux états possibles : sortie pour
le balayage des bordures et rentrée pour le nettoyage des surfaces.


#### Direction du nettoyage des surfaces et découpage de la zone principale

Dans cette première version, nous avons choisi de nettoyer toutes les surfaces selon la même direction, et en utilisant
la direction donnée par le plus grand coefficient de la première transformée de Hough. Dans certains cas, cette
direction n’est pas la meilleure, comme le montre le contre-exemple sur la [@fig:diagonale].

![Exemple d’une salle où la bonne direction de balayage serait en diagonale, alors que le mur le plus long est
horizontal](imgs/diag.png){#fig:diagonale height=7cm}

Par ailleurs, il peut être bon de découper la zone principale en sous-zones présentant des directions générales
différentes. Un algorithme de découpage d’une zone non-convexe a déjà été développé au sein de l’équipe Gepetto dans le
cadre du travail d’engins agricoles dans [@decoupage], dont est extrait la [@fig:decoupage].

![Exemple d’algorithme de planification de trajectoires pour engin agricole dans des polygones non
convexes](imgs/decoupage.png){#fig:decoupage height=7cm}

#### Ordre de parcours des portions de trajectoires

Un dernier axe d’amélioration serait d’optimiser l’ordre de parcours des portions de trajectoires de balayage des
bordures et de nettoyage des surfaces.

Dans un premier temps, une modification d’algorithmes classiques de recherche opérationnelle pourrait permettre de
mieux prendre en compte la possibilité de parcourir les trajectoires de nettoyage des surfaces dans un sens ou dans
l’autre, ainsi que de pallier le problème de la recherche de la trajectoire suivante si sa configuration initiale est
trop loin pour notre RRT-Connect.

Dans un second temps, l’idéal serait de pouvoir découper certaines trajectoires de balayage des bordures pour aller
balayer un obstacle proche d’un long mur, comme dans la [@fig:pilierrond].

![Dans cet exemple, il serait intéressant de pouvoir balayer les bords des piliers ronds en s’arrêtant à mi-chemin sur
les trajectoires de balayage des murs verticaux](imgs/pilier.png){#fig:pilierrond height=7cm}
