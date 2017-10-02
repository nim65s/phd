#### Résultats

\centering

![](imgs/lemon/demo.png){height=5cm}

<div class="columns">
<div class="column" width="33%">
@[BA Robotic Systems](imgs/people/bars.png)
</div>
<div class="column" width="33%">
@[Florent Lamiraux: LAAS-CNRS](imgs/people/fl.jpg)
</div>
<div class="column" width="33%">
@[Jean-Paul Laumond: LAAS-CNRS](imgs/people/jpl.jpg)
</div>
</div>

<div class="notes">

L’implémentation de notre méthode dans un simulateur donne des résultats tout à fait satisfaisants, mais les
démonstrations réelles sur le robot n’ont pas été aussi bonnes pour deux raisons principales.

La première de ces raisons est le format initialement choisi pour que nous indiquions à BA les mouvements à
éxécuter par le robot. En effet, nous avions convenu de leur fournir une trajectoire discrétisée, que leur
asservissement doit ensuite essayer de suivre. Le problème, c’est que cettediscrétisation s’effectue au prix d’une
perte d’information, et on perd par exemple systématiquement la localisation théorique exacte de chaque point de
rebroussement. Il est devient donc très difficile pour l’asservissement du robot de suivre cette trajectoire fournie,
puisque nous utilisons toujours le rayon de courbure minimal possible.

La seconde de ces raisons concerne le choix initial de la classe du robot. Pour qu’un robot de classe (1, 1)
puisse suivre une trajectoire comprenant un point de rebroussement, il est nécessaire que le robot s’arrête au niveau
de ce point pendant la durée nécessaire à la réorientation de sa roue d’un extrême à l’autre, exactement comme lorsque
que vous faites un créneau avec votre voiture. Combiné avec le problème précédent, cela rend l’asservissement
pratiquement impossible.

Ces deux problèmes sont liés, et seraient de plus relativement simple à résoudre, s’il était possible de reprendre à
zéro la conception de ce projet, ce qui n’est pas du tout évident dans un contexte industriel.

TODO: On n’a pas bien eu les contraintes, on s’est mal compris

</div>
