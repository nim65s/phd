# Étude de la robotique mobile {#sec:mobile}

\input{manuscript/partstart}

## Introduction : Les robots à roues {-}

Comme nous l’avons vu dans l’introduction générale, la robotique est déjà bien présente dans notre quotidien.

Pour autant, la recherche en robotique est loin d’être terminée. Citons par exemple les efforts humains et financiers
actuellement fournis par des entreprises comme Tesla, Google ou Uber, ainsi que de plus en plus de constructeurs
automobiles plus conventionnels, qui œuvrent à robotiser nos moyens de transports.

Afin de mieux comprendre comment la robotique permet à des systèmes de se mouvoir, nous étudierons dans cette partie la
locomotion en robotique mobile, et plus particulièrement les robots à roues.

La roue est le premier et le plus simple des systèmes créés par l’homme pour assurer des fonctions de déplacement.
Elle est caractérisée par un contact de roulement sans glissement, ce qui implique une contrainte dite de non-holonomie
sur les déplacements du robot qu’elle supporte.

Avec différents types de roues, positionnées suivant diverses combinaisons, un robot peut se déplacer de différentes
manières dans le plan. Pour étudier ces différents types de robots, nous reprendrons la classification de @campion96.

Cette classification repose sur l’étude des différents types de roues, puis celle de la structure des modèles
cinématiques et dynamiques de robots actionnés par ces roues. En introduisant les concepts de degré de mobilité et de
degré de dirigeabilité d’un robot mobile, elle démontre que les robots mobiles peuvent être répartis en cinq classes.

Un robot mobile a donc un degré de mobilité $\delta_m$, compris entre 1 et 3, correspondant au nombre de degrés de
liberté pouvant être directement actionnés. On lui attribue également un degré de dirigeabilité $\delta_s$, compris
entre 0 et 2, indiquant le nombre de roues pouvant être indépendamment réorientées pour diriger le robot.

La somme de ces deux nombres correspond au degré de manœuvrabilité du robot $\delta_M = \delta_m + \delta_s$, compris
entre 2 et 3, indiquant le nombre total de degrés de liberté dont il dispose dans son mouvement dans le plan.

On a alors cinq classes de robots mobiles, notées $(\delta_m, \delta_s)$, présentées dans la [@tbl:campion].

$\delta_M$ 3 2 3 2 3
---------- - - - - -
$\delta_m$ 3 2 2 1 1
$\delta_s$ 0 0 1 1 2
---------- - - - - -

: Cinq classes de robots mobiles, d’après @campion96. {#tbl:campion}

Dans la suite de cette partie, nous montrerons dans le chapitre [-@sec:offroad] un exemple d’application pour des
robots différentiels, c’est-à-dire munis principalement de deux roues motorisées, fixes, et sur le même axe
([@fig:differentiel]). Puis, nous étudierons dans le chapitre [-@sec:lemon], un exemple de robots munis de deux roues
fixes et d’une tourelle, qui est une roue dont le plan dans lequel elle tourne est orientable autour d’un axe passant
par son centre ([@fig:carlike]). Enfin, dans le chapitre [-@sec:transhumus], nous terminerons cette partie avec un
exemple de robots munis de trois tourelles ([@fig:omni]).

<div id="fig:mobiles">
![Différentiel (2, 0)](tikz/differentiel.pdf){#fig:differentiel height=4.5cm}
![Car-like (1, 1)](tikz/carlike.pdf){#fig:carlike height=4.5cm}
![Omnidirectionnel (1, 2)](tikz/omni.pdf){#fig:omni height=4.5cm}

Trois classes de robots mobiles étudiés dans cette partie. Dans ces schémas, les flèches représentent les degrés de
liberté des roues, parmi lesquels on retrouve ceux qui sont actionnés en rouge et gras.
</div>

Le robot omnidirectionnel ayant plus d’actionneurs que de degré de manœuvrabilité, il est bien sûr nécessaire
d’asservir certains de ces actionneurs par rapport aux autres. En d’autres termes, en pratique, trois actionneurs
définissent le mouvement, et les autres se contentent de suivre, afin d’éviter des problèmes de stabilité.

Ces robots sont respectivement de type $(2, 0)$, $(1, 1)$ et $(1, 2)$. Nous verrons alors l’impact de la répartition
des degrés de mobilité et de dirigeabilité lorsque le degré de manœuvrabilité est constant, puis l’impact de l’ajout
d’un degré de dirigeabilité lorsqu’on ne change pas le degré de mobilité sur la planification de mouvement d’un robot.

\input{manuscript/partend}
