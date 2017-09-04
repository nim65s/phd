### Optimisation {#sec:optimisation}

Les premiers résultats de la méthode présentée dans les sections précédentes ont permis de remplir le cahier des
charges. Cependant, il est facile pour un observateur humain d’imaginer de meilleures options que la trajectoire finale
générée. Regarder le robot suivre sa trajectoire est donc un peu frustrant.

Les trajectoires générées par l’algorithme de Reeds and Shepp peuvent parfois surprendre, comme le montre l’exemple de
trajectoire généré de la [@fig:toolong], et l’algorithme de tir aléatoire peut facilement rater une transition qui
semble simple à un humain, malgré notre utilisation d’une méthode de raccourcis aléatoires.

![Exemple de trajectoire de suivi des murs générée par l’algorithme de Reeds and Sheep étonnamment
longue.](imgs/toolong.png){#fig:toolong width=100%}

Notre objectif est alors de raccourcir au maximum la longueur de la trajectoire finale, quitte à relaxer un peu la
contrainte de couverture de la surface.

Pour cela, nous remarquons que dans le cas classique d’un angle droit entre deux murs, le robot balaye le premier mur
jusqu’à la collision avec le second, puis fait marche arrière, va se placer parallèlement au second, refait marche
arrière jusqu’à la collision avec le premier, puis commence le balayage du second.

Cette manœuvre parait naturelle si l’on cherche à tout nettoyer au mieux, mais demande beaucoup de temps. On nous
demande alors de tronquer la fin de la première trajectoire de balayage des bordures et le début de la seconde.

Nous relions ensuite ces deux configurations par une trajectoire dite de @dubins, qui est optimale pour un
robot mobile à tourelle ayant un rayon de giration borné et ne se déplaçant qu’en marche avant[^9], évitant ainsi les
manœuvres.

[^9]: En pratique, vu que le robot balaye en marche arrière, nous parlons plutôt d’une trajectoire de Snibud.

Cette stratégie est illustrée sur la [@fig:dubins]

<div id="fig:dubins">
![Avant: Trajectoires complètes de balayage des murs, reliées par une trajectoire de Reeds and
Sheep.](imgs/avant.png){height=7cm}
![Après: Trajectoires tronquées de balayage des murs dans l’angle droit, reliées par une trajectoire de
Dubins. On remarque que certaines trajectoires sont inutilement tronquées, puisqu’elles n’aboutissent pas sur un
obstacle.](imgs/apres.png){height=7cm}

Illustration du raccourci utilisé. Cette stratégie est surtout utile dans les angles droits fermés, mais elle réduit
inutilement les segments de balayage des bordures dans d’autres cas.
</div>

Dans le cas d’un angle droit, cette solution donne les bons résultats auxquels nous nous attendions. Mais en pratique,
il faut garder à l’esprit que cela ajoute un paramètre supplémentaire à régler, à savoir la longueur tronquée sur
chaque trajectoire (voire deux si on veut des longueurs tronquées différentes).

Or la valeur optimale de ce paramètre dépend grandement d’autres paramètres, et notamment de l’angle entre deux murs
successifs, de la longueur initiale des trajectoires avant troncage, et de la distance nécessaire entre le robot et le
mur pour pouvoir tourner directement sans engendrer de collision.

Enfin, cette technique ne fonctionne pas sur toutes les transitions, comme le montre la [@fig:toolong-better].

![Amélioration de l’exemple de la [@fig:toolong]. Dans certains cas, la méthode de Dubins raccourcit grandement les
trajectoires, mais elle n’est pas toujours applicable.](imgs/toolong-better.png){#fig:toolong-better width=80%}

\newpage
