# Étude de la robotique mobile {#sec:mobile}

## Introduction: Les robots à roues {-}

Comme nous l’avons vu, la robotique est déjà bien présente dans notre quotidien. Pour autant, la recherche en robotique
est loin d’être terminée. Citons par exemple les efforts humains et financiers actuellement fournis par des entreprises
comme Tesla, Google ou Uber, ainsi que de plus en plus de constructeurs automobiles plus conventionnels, qui
travaillent à robotiser nos moyens de transports.

Afin de mieux comprendre comment la robotique permet à des systèmes de se mouvoir, nous étudierons dans cette partie la
robotique mobile, et plus particulièrement les robots à roues.

La roue est le premier et le plus simple des systèmes créés par l’homme pour assurer des fonctions de déplacement.
Elle est caractérisée par un contact de roulement sans glissement, ce qui implique une contrainte non-holonome sur les
déplacements du robot qu’elle supporte.

Avec différents types de roues, positionnées suivant diverses combinaisons, un robot peut se déplacer de différentes
manières dans le plan. Pour étudier ces différents types de robots, nous reprendrons la classification de [@campion96].

Cette classification repose sur l’étude des différents types de roues, puis celle de la structure des modèles
cinématiques et dynamiques de robots constitués de ces roues. En introduisant les concepts de degré de mobilité et de
degré de dirigeabilité d’un robot mobile, elle démontre que les robots mobiles peuvent être répartis en cinq classes.

Un robot mobile a donc un degré de mobilité $\delta_m$, compris entre 1 et 3, correspondant au nombre de degrés de
liberté pouvant être directement actionnés. On lui attribue également un degré de dirigeabilité $\delta_s$, compris
entre 0 et 2, indiquant le nombre de roues pouvant être indépendamment réorientées pour diriger le robot.

La somme de ces deux nombres correspond au degré de manœuvrabilité du robot $\delta_M = \delta_m + \delta_s$, compris
entre 2 et 3, indiquant le nombre total de degrés de liberté dont il dispose dans son mouvement dans le plan.

On a alors cinq types de robots mobiles, notés $(\delta_m, \delta_s)$:

$\delta_M$ 3 2 3 2 3
---------- - - - - -
$\delta_m$ 3 2 2 1 1
$\delta_s$ 0 0 1 1 2
---------- - - - - -

: Cinq classes de robots mobiles, d’après [@campion96]

Dans la suite de cette partie, nous donnerons dans le chapitre [-@sec:offroad] un exemple de robots différentiels,
c’est-à-dire munis principalement de deux roues fixes sur le même axe. Puis, nous étudierons dans le chapitre
[-@sec:lemon], un exemple de robots munis de deux roues fixes et d’une tourelle, qui est une roue dont le plan dans
lequel elle tourne est orientable autour d’un axe passant par son centre. Enfin, dans le chapitre [-@sec:transhumus],
nous terminerons cette partie avec un exemple de robots munis de trois tourelles.

Ces robots sont respectivement de type $(2, 0)$, $(1, 1)$ et $(1, 2)$. Nous verrons alors l’impact de la répartition
des degré de mobilité et de dirigeabilité lorsque le degré de maœuvrabilité est constant, puis l’impact de l’ajout d’un
degré de dirigeabilité lorsqu’on ne change pas le degré de mobilité sur la planification de mouvement d’un robot.
