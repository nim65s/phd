### Optimisation {#sec:optimisation}

Les premiers résultats de la méthode présentée dans les sections précédente ont permis de remplir le cahier des
charges. Cependant, il est facile à un observateur humain de trouver des optimisations de la trajectoire finale
générée.

Les trajectoires générées par l’algoritme de Reeds and Shepp peuvent parfois surprendre, commme le montre l’exemple de
trajectoire généré de la [@fig:toolong], et l’algorithme de tir aléatoire peut facilement rater une transition qui
semble simple à un humain malgré notre utilisation d’une méthode de raccourcis aléatoires.

![Exemple de trajectoire de suivi des murs générée par l’algorithme de Reeds and Sheep étonnament
longue](imgs/toolong.png){#fig:toolong width=100%}

Notre objectif est alors de raccourcir au maximum la longueur de la trajectoire finale, quitte à relaxer un peu la
contrainte de couverture de la surface.

Pour cela, nous remarquons que dans le cas classique d’un angle droit entre deux murs, le robot balaye le premier mur
jusqu’à la collision avec le second, puis fait marche arrière, va se placer parrallèlement au second, refait marche
arrière jusqu’à la collision avec le premier, puis commence le balayage du second.

Cette manœuvre parait naturelle, mais demande beaucoup de temps. Nous choisissons alors de tronquer la fin de la
première trajectoire de balayage et le début de la seconde.

Nous relions ensuite ces deux configurations par une trajectoire de Dubins[^8] [@dubins], qui est optimale pour un
robot mobile à tourelle ayant et rayon de giration borné et ne se déplaçant qu’en marche avant.

[^8]: En pratique, vu que le robot balaye en marche arrière, nous parlons plutôt d’un algorithme de Snibud.

Cette stratégie est illustrée sur la [@fig:dubins]

<div id="fig:dubins">
![Avant: Trajectoires de balayage des murs complètes reliées par une trajectoire de Reeds and Sheep](imgs/avant.png){height=5cm}
![Après: Trajectoires de balayage des murs tronquées dans l’angle droit reliées par une trajectoire de
Dubins](imgs/apres.png){height=5cm}

Illustration du raccourci utilisé dans les angles droits.
</div>

<!--TODO: refaire ces figures-->

Dans le cas d’un angle droit, cette solution donne de bons résultats. Mais en pratique, il faut garder à l’esprit que
cela ajoute un paramètre supplémentaire à régler, à savoir la longueur tronquée sur chaque trajectoire (voire deux si
on veut des longueurs tronquées différentes).

Or la valeur optimale de ce paramètre dépend grandement d’autres paramètres, et notamment de l’angle entre deux murs
successifs, la longueur initiale des trajectoires à tronquer, et la distance nécessaire entre le robote et le  mur pour
pouvoir tourner sans collisions.
