# Étude de la robotique mobile

## Introduction: Les robots à roues {-}

La robotique consiste à augmenter l’autonomie d’un système, en lui donnant des facultés de perception, de décision et
d’action.

Grâce à un savant mélange d’électronique, d’informatique, de mécanique, de mathématiques, d’automatique, et de bien
d’autres domaines, elle est aujourd’hui bien au-delà du stade de science fiction, où elle était encore il y a quelques
décennies à peine.

On lui trouve de nos jours aisément des applications dans tous les domaines de l’industrie, que soit soit pour la
fabrication, la manutention, ou le contrôle qualité. En remplaçant l’homme dans des tâches difficiles, répétitives,
fastidieuses, voire dangereuses, elle démontre son impact sur la société ainsi que son intérêt économique.

Pour autant, la recherche en robotique est loin d’être terminée. Citons par exemple les efforts humains et financiers
actuellement fournis par des entreprises comme Tesla, Google ou Uber, ainsi que de plus en plus de constructeurs
automobiles plus conventionnels, qui travaillent sans relâche à robotiser nos moyens de transports.

Afin de mieux comprendre comment la robotique permet à des systèmes de se mouvoir, nous étudierons dans cette partie la
robotique mobile, et plus particulièrement les robots à roues.

La roue est le premier et le plus simples des systèmes créés par l’homme. Elle est caractérisée par un contact de
roulement sans glissement, ce qui implique une contrainte non-holonome sur les déplacements du robot qu’elle supporte.

Avec différents types de roues, positionnées suivant diverses combinaisons, un robot peut se déplacer de différentes
manières dans le plan. Pour étudier ces différents types de robots, nous reprendrons la classification de [@campion96].

Un robot mobile a donc un degrés de mobilité $\delta_m$, compris entre 1 et 3, correspondant au nombre de degrés de
liberté pouvant être directement actionnés. On lui attribue également un degré de dirigeabilité $\delta_s$, compris
entre 0 et 2, indiquant le nombre de roues pouvant être indépendamment réorientées pour diriger le robot. La somme de
ces deux nombres correspond au degré de manœuvrabilité du robot $\delta_M = \delta_m + \delta_s$, compris entre 2 et 3,
indiquant le nombre total de degrés de liberté dont il dispose dans son mouvement dans le plan.

Dans la suite de cette partie, nous étudierons dans le chapitre \ref{clemon} un exemple de robot munit de deux roues
fixes et d’une tourelle (roue orientable), puis dans le chapitre \ref{ctranshumus} un exemple de robot munit de trois
tourelles.

Ces deux types de robots ont un $\delta_m = 1$. Cependant, dans le premier cas, $\delta_s = 1$, et dans le second
$\delta_s = 2$. Nous verrons alors l’impact de l’ajout d’un degré de dirigeabilité sur la planification de mouvement
d’un robot.
