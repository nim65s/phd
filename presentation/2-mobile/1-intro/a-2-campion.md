#### Cinq classes de robots mobiles

\centering

G. Campion, G. Bastin, et B. D’Andrea-Novel: « Structural properties and classification of kinematic and dynamic models
of wheeled mobile robots ».  IEEE Transactions on Robotics and Automation, 1996.

-------------- --- --- --- --- ---
mobilité        2   1   1   2   3
dirigeabilité   0   1   2   1   0
-------------- --- --- --- --- ---

. . .

<div class="columns" pos="b">
<div class="column" width="20%">
![(2, 0)](tikz/differentiel.pdf)
</div>
<div class="column" width="20%">
. . .

![(1, 1)](tikz/carlike.pdf)
</div>
<div class="column" width="20%">
. . .

![(1, 2)](tikz/omni.pdf)
</div>
<div class="column" width="20%">
. . .

![(2, 1)](tikz/deuxun.pdf)
</div>
<div class="column" width="20%">
![(3, 0)](tikz/troiszero.pdf)
</div>
</div>



<div class="notes">
En analysant ces différents types de roues et les différents combinaisons qu’il est possible d’en faire pour créer un
robot mobile, il est montré dans cet article qu’il existe cinq classes de robots mobiles. Pour cela, on introduit les
notions de degré de mobilité et dirigeabilité d’un robot.

Le degré de mobilité correspond au nombre de degrés de libertés pouvant être directement contrôlés, et le  degré de
dirigeabilité et correspond au nombre de roues pouvant être indépendamment réorientées afin de diriger le robot.

À partir des différentes combinaisons possibles entre ces deux nombres, on obtient la classe d’un robot. Dans la suite
de cette partie, nous verrons des projets mettant en œuvre des robots des trois premières de ces classes.

Prenons par exemple la classe (2, 0), représentant donc les robots mobiles à deux degrés de mobilité et 0 degrés de
dirigeabilité. Ces robots, que l’on appelle communément des robots différentiels, sont les plus simple à contrôler.
Ils sont principalement constitués de deux roues co-axiales indépendamment motorisées, et la différence de vitesse de
ses roues influe directement sur la trajectoire qui sera suivie par le robot.
</div>
