### Contrôle optimal pour le design et le contrôle {#sec:yoyosolv}

Le contrôle optimal est un puissant outil mathématique générique qui permet de trouver une solution particulière parmi
une infinité de possibilités. Ces dernières années, des cadres fiables et efficaces de contrôle optimal sont apparus,
permettant de contrôler des systèmes complexes de grandes dimensions [@leineweber03;@acado].

Dans notre cas, la recherche simultanée des paramètres du modèle et du contrôle est posée comme un problème de contrôle
optimal pour une fonction de coût donnée. Cette fonction de coût représente l’objectif de la démarche et peut être
n’importe quelle fonction dont les valeurs sont des réels.

Comme exemples de fonction de coût pour des marcheurs passifs, on retrouve le coût de transport ou le temps minimal. De
plus, nous ajoutons la possibilité de laisser la durée du mouvement comme étant l’un des paramètres libres du problème.

D’autres paramètres libres, comme la longueur d’un pas ou la pente du sol peuvent être ajoutés dans la liste des
paramètres.

#### Notations

Nous notons $\bm x \triangleq (\bm q, \bm{\dot q})$ l’état du système, $\bm u$ le vecteur de contrôle et $\bm p$ le
vecteur des paramètres, composé à la fois des paramètres du modèle et des paramètres libres susmentionnés.

Les trajectoires d’état et de contrôle sont respectivement notées $\underline{\bm x}$ et $\underline{\bm u}$

La fonction de coût et la dynamique du système sont respectivement notées $\ell(t, \bm x, \bm u, \bm p)$ et $\frac{d\bm
x}{dt} = f(t, \bm x, \bm u, \bm p)$. Nous utilisons ici les mêmes notations pour noter à la fois la dynamique continue
et la dynamique d’impact.

Enfin, $g(t, \bm x, \bm u, \bm p)$ correspond aux contraintes d’inégalités qui doivent être vérifiées tout au long de
la trajectoire. Des contraintes d’égalité pourraient également être ajoutées sans nuire à la généralité de notre
démarche.

Comme nous l’avons vu dans la [@sec:contcont], la fonction $g$ est essentiellement composée des contraintes sur le
cône de frottement.

#### Formulation du problème de contrôle optimal

La dynamique hybride  des marcheurs passifs peut être considérée comme un système multi-phases, comprenant des phases
de simple et double support et d’impact. Dans la suite, l’entier $s$ correspond à l’index de la $s$^ème^ phase.

Le problème générique de contrôle optimal pour déterminer simultanément les paramètres du modèle et du contrôleur peut
donc être écrit comme dans l’[@eq:opcon]

$$\begin{aligned}
\underset{\substack{\hspace{0em} \underline{\bm x}, \underline{\bm u}, \bm p}}{\min } \ \ \
& & \hspace{2em} {\sum_{s=1}^S} \int_{t_{s}}^{t_{s}+\Delta t_s\hspace{-4em}} \ell_{s} (t,\bm x, \bm u,
\bm p) \, dt \\
\text{s.t.} & & \dot{\bm{x}} = f_{s}(t, \bm x, \bm u, \bm p), \forall t \in [t_{s},t_{s}+\Delta t_s] \\
& & g_{s}(t, \bm x, \bm u, \bm p) \geq \bm 0,  \forall t \in [t_{s},t_{s}+\Delta t_s] \\
& & \pi(\underline{\bm x}, \underline{\bm u}, \bm p) \geq \bm 0
\end{aligned} $$ {#eq:opcon}

Dans l’[@eq:opcon], $\pi$ est une fonction qui agit à a fois sur les trajectoires d’état et de contrôle pour garantir
les contraintes de périodicité. $\Delta t_s$ est la durée de la phase $s$, et $T=\sum \Delta t_s$ est la durée totale
du mouvement.

Dans le cas d’un impact, la durée de la phase est réduite à 0.

#### Résoudre le problème de contrôle optimal

Deux principales méthodes existent pour résoudre le problème de dimension infinie [@eq:opcon].

La première méthode et dite méthode indirecte. Elle consiste à exploiter les conditions nécessaires d’optimalité, à
savoir le principe du maximum de Pontryagin [@liberzon12], qui transforme le problème [@eq:opcon] en un problème à
valeurs bornées d’équations différentielles classiques. Cependant, cette méthode n’est pas capable de gérer les
contraintes de trajectoire.

La seconde méthode est dite directe. Cette méthode commence par discrétiser le problème initial en un problème
d’optimisation non linéaire (NLP) de dimensions finies, qui est alors résolu avec des stratégies standard pour des NLP.
Parmi ces stratégies, on en retrouve trois principales: le *single shooting*, la *collocation* et le *multiple
shooting*.

Dans la suite de cette section, nous présentions succinctement  ces trois méthodes. Pour plus de détails, on peut se
reporter à [@FastMS].

##### Single Shooting

Cette méthode discrétise le contrôle et les contraintes suivant une grille temporelle. La trajectoire de l’état est
retrouvée par intégration de la trajectoire discrète du contrôle suivant cette grille.

Cette méthode réduit le NLP à la recherche d’une trajectoire de contrôle, donc le problème d’optimisation est de
faible dimension. Cependant, le solveur est difficile à initialiser si l’on dispose seulement d’une estimation
initiale sur la trajectoire de l’état, et peut ne pas converger du tout dans le contexte de systèmes non stables.

##### Collocation

Cette méthode discrétise à la fois les trajectoires de contrôle et d’état suivant une grille temporelle. Pour cette
méthode, la trajectoire de l’état assure la partie dynamique de l’[@eq:opcon] à chaque nœud de la grille. Le problème
peut donc alors facilement être initialisé à partir d’une trajectoire d’état donnée, et la collocation gère bien les
dynamiques instables.

Cependant, une grille très fine est nécessaire pour rapprocher la trajectoire d’état de la dynamique réelle du système.

##### Multiple Shooting

Cette méthode profite des deux précédentes. Elle utilise une grille temporelle plus grossière. Sur chaque intervalle,
le contrôle et l’état initial sont discrétisés. L’état final de l’intervalle est alors obtenu par l’intégration de la
dynamique du système.

De cette manière, chaque intervalle est indépendant de ses voisins. Les dépendances entre les intervalles successifs
sont transférées en tant que contraintes d’égalité du NLP.

Le NLP reste à faible dimension et peut facilement être initialisé à partir d’une trajectoire d’état.

De plus, le multiple shooting est particulièrement adapté aux systèmes multi-phases, puisque les phases sont
indépendantes les unes des autres.

Enfin, le multiple shooting a déjà été utilisé avec succès pour la modélisation de la course humaine [@schultz10].

D’après ces avantages, nous choisissons cette stratégie pour résoudre le problème [@eq:opcon].

#### Solveur pour contrôle optimal

Notre méthode repose sur l’utilisation du logiciel MUSCOD-II [@leineweber03], un solveur utilisant la méthode du
multiple shooting prévu pour les systèmes hautement non-linéaires soumis à des contraintes d’égalité et d’inégalités
sur les trajectoires, développé dans le groupe d'Optimisation et de Simulation de l’université d’Heidelberg.

MUSCOD-II gère efficacement  les systèmes multi-phases avec des dynamiques discontinues et des contraintes de
périodicité.

Cependant, MUSCOD-II n’est pas un logiciel libre. Il reste possible de le remplacer par ACADO [@acado], qui implémente
des fonctionnalités similaires.
