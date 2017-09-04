### Premières expériences de test {#sec:exptest}

Dans cette section, nous décrivons la première expérience de test de notre méthode. Les résultats de cette expérience
sont énoncés dans la section suivante, [@sec:restest]

La généralité de notre méthode est illustrée dans les divers exemples fournis dans la [@tbl:results]. Ces exemples
incluent différentes structures cinématiques et différents types de contrôle.

De cette manière, nous pouvons comparer différents topologies de chaînes polyarticulées, et, pour une topologie donnée,
comparer différentes méthodes de contrôle, utilisant des actionneurs actifs ou bien passifs. Une fois qu’une topologie
est choisie, nous montrons qu’il est possible de remplacer un actionnement actif par un simple amortisseur.

Le mouvement des cinq premiers robots donnés dans la [@tbl:results] est contraint au plan sagittal. Cette restriction
est supprimée pour le sixième robot, qui évolue dans l’espace 3D.

#### Entrées et sorties

La [@fig:framework] montre les entrées et sorties générales de notre système. Dans les expériences données dans le
[@tbl:results], les entrées sont:

- la structure cinématique du robot;
- des paramètres anthropométriques pour les corps attachés aux articulations de cette structure;
- une fonction de coût définie dans la [@sec:costfunc];
- des contraintes définies dans la [@sec:constraints];
- une méthode d’actionnement définie dans la [@sec:actuation].

Dans ces expériences, nous choisissons de fixer à la fois la durée d’un pas à 0,8 secondes et une pente descendante
inclinée de 0,05 radians pour chaque scénario, et laissons le solveur optimiser la longueur d’un pas, tout en la
limitant à l’intervalle $[0.4,1]$ mètres.

Les sorties de notre système sont le coût optimal de transport, ainsi que la longueur du pas et les trajectoires d’état
et de contrôle associées.

Nous étudions également le nombre d’itérations nécessaire au solveur pour converger ainsi que la durée de cette
résolution.

#### Fonction de coût {#sec:costfunc}

Nous utilisons la même fonction de coût dans chaque scénario. Cette fonction de coût correspond au classique coût de
transport (CoT). Le CoT est une quantité sans dimensions que reflète l’efficacité énergétique d’une méthode de
locomotion.

Par définition, le CoT est le ratio entre l’énergie $E$ consommée par le système et sa masse $mg$ multipliée par la
distance parcourue $d$, comme le montre l’[@eq:cot].

$$ \text{CoT} \triangleq \cfrac{E}{mgd} $$ {#eq:cot}

Dans l’[@eq:cot], $m$ est la masse du système. L’énergie $E$ qu’il consomme est la somme des énergies potentielle $mgh$
(où $h$  est la variation de l’altitude du centre de masse) et de l’intégrale de la puissance consommée par les
actionneurs, donnée dans l’[@eq:energy].

$$ E_A = \int\limits_{t=0}^T\|\mathbf{\dot q}^+ - \mathbf{\dot q}^-\|_M\delta+\mathbf\tau\cdot\mathbf{\dot q}dt $$ {#eq:energy}

Dans cette [@eq:energy], $\delta$ est l'impulsion de Dirac correspondant à l’impact, $\cdot$ est l’opérateur de produit
scalaire, et $\|\mathbf x\| \triangleq \sqrt{\mathbf x^\top M\mathbf x}$.

Sur une pente d’angle $\alpha$, nous pouvons donc écrire le CoT suivant l’[@eq:cota].

$$ \text{CoT} = \sin\alpha + \int\limits_{t=0}^T\cfrac{\|\mathbf{\dot q}^+ - \mathbf{\dot
q}^-\|_M\delta+\mathbf\tau\cdot\mathbf{\dot
q}}{mgd}dt $$ {#eq:cota}

Cette fonction de coût est ici utilisée comme un exemple pour les différents cas vus dans la [@sec:restest] ; dans des
cas réels, le choix d’une meilleure fonction de coût reste un problème ouvert.

De plus, les CoT que nous obtenons ne sont pas destinés à être comparés avec d’autres exemples, dans la mesure où nous
ne considérons que des systèmes parfaits, sans frottements ni pertes lors de conversion d’énergies.

#### Contraintes {#sec:constraints}

Pour réduire les dimensions du NLP, nous calculons la solution du problème pour un demi-pas, grâce à la périodicité et
la symétrie entre les segments gauches et droits.

Nous contraignons alors la jambe qui se balance à être en contact avec le sol  uniquement au début et à la fin de la
simulation. Ensuite, la cyclicité et la symétrie du mouvement est assurée par des contraintes périodiques sur les
configurations, vitesses et couples initiaux et finaux.

#### Actionnement {#sec:actuation}

Dans une première étape, nous utilisons un actionnement actif. La trajectoire du couple appliqué à chaque articulation
lors de la marche est alors modélisée par des splines d’ordre trois.

Une implémentation matérielle aurait alors besoin d’une source d’énergie, comme une batterie ou une bonbonne d’air
comprimé, ainsi que d’un contrôleur pouvant délivrer le couple désiré.

Dans une seconde étape, nous comparons cet actionnement actif à un actionnement passif, qui consiste simplement en un
contrôleur Proportionnel Dérivé (PD) réalisé à partir d’un ressort et d’un amortisseur. Dans ce cas, le couple $\tau_j$
appliqué à l’articulation $j$ est donné par l’[@eq:tauj].

$$ \tau_j = - P_j(q_j - Q_j) - D_j \dot q_j $$ {#eq:tauj}

Dans l’[@eq:tauj], $q_j$ est la configuration de l’articulation $j$, et $\dot q_j$ sa vitesse. $P_j$ est la raideur
du ressort associé à l’articulation $j$, $Q_j$ sa longueur libre, et $D_j$ le coefficient d’amortissement. Ces
trois paramètres sont optimisés par le solveur.

À partir de ces paramètres, il est théoriquement possible de fabriquer un marcheur purement passif. Dans ce cas, la
gravité est la seule source d’énergie.

Naturellement, nous contraignons le solveur à utiliser les mêmes coefficients pour les articulations symétriques.

#### Paramètres des corps rigides

Tous les robots présentés dans ces résultats utilisent des paramètres fixés et anthropométriques pour ce qui est des
tailles des segments, de leurs masses, de la position de leur centre de masse et de leurs matrices d’inertie, calculés
à partir d’une taille et d’un poids de référence gardé constant entre les différents tests. Ces paramètres suivent les
tables anthropométriques données par @dumas07.

Notre modèle minimal $M_A$ est composé d’un bassin, de deux cuisses et deux jambes, où seules les hanches sont
actionnées. Dans le modèle $M_B$, les genoux sont également actionnés.

Au-dessus de cette base, nous ajoutons dans les modèles $M_C$, $M_D$ et $M_E$ un torse et une tête. Le cou n’est
actionné que dans le modèle $M_D$.

Enfin, nous ajoutons deux bras et deux avant-bras dans le modèle $M_E$ avec des épaules actionnées.

Toutes les articulations actionnées sont des liaisons pivot d’axes parallèles.
