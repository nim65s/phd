#### Cinq classes de robots mobiles

\centering

<div class="columns" pos="b">
<div class="column" width="20%">
\centering
Offroad

![(2, 0)](tikz/differentiel.pdf)
</div>
<div class="column" width="20%">
\centering
Lemon

![(1 ,1)](tikz/carlike.pdf)
</div>
<div class="column" width="20%">
\centering
Transhumus

![(1, 2)](tikz/omni.pdf)
</div>
<div class="column" width="20%">
![(2, 1)](tikz/deuxun.pdf)
</div>
<div class="column" width="20%">
![(3, 0)](tikz/troiszero.pdf)
</div>
</div>


G. Campion, G. Bastin, et B. D’Andrea-Novel: « Structural properties and classification of kinematic and dynamic models
of wheeled mobile robots ».  IEEE Transactions on Robotics and Automation, 1996.

<div class="notes">

En analysant ces différents types de roues et les différents combinaisons qu’il est possible d’en faire pour créer un
robot mobile, il est montré dans cet article qu’il existe cinq classes de robots mobiles. Pour cela, on introduit les
notions de degré de mobilité et dirigeabilité d’un robot, et on désigne les différentes classes à l’aide d’un couple de
ces nombres.

Le premier nombre est le degré de mobilité, et correspond au nombre de degrés de libertés pouvant être directement
contrôlés. Le second est de degré de dirigeabilité et correspond au nombre de roues pouvant être indépendamment
réorientées afin de diriger le robot.

Prenons par exemple la classe (2, 0), représentant donc les robots mobiles à deux degrés de mobilité et 0 degrés de
dirigeabilité. Ces robots, que l’on appelle communément des robots différentiels, sont les plus simple à contrôler.
Ils sont principalement constitués de deux roues motrices co-axiales, et la différence de vitesse de ses roues influe
directement sur la trajectoire qui sera suivie par le robot. Nous verrons plus en détails de tels robots dans le projet
Offroad.

Si l’on considère ensuite la classe (1, 1), nous avons des robots pouvant se comporter comme des voitures. La
principale différence avec les robots précédents est que leur rayon de braquage est limité. Cette borne dépend
notamment de la distance entre les roues fixes et les roues orientables d’un tel robot. Nous avons utilisé de tels
robots pour le projet Lemon.

La troisième classe de robot utilisée au cours de cette thèse est la classe (1,2). Avec leurs deux degrés de
dirigeabilité, ces robots peuvent faire évoluer indépendament leur direction et leur vitesse angulaire, lorsque leur
degré de mobilité influe sur leur vitesse linéaire, comme nous le verrons dans le projet Transhumus.

</div>


