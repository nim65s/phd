### Résultats des tests {#sec:restest}

Dans cette section, nous présentons les résultats des six expériences présentées dans la [@tbl:results] sous forme de
cinq comparaisons.

Ces comparaisons servent à illustrer le potentiel et l’utilité de la méthode, et ne doivent pas être sorties de ce
contexte d’illustration.

#### Influence des genoux

L’influence de l’actionnement des genoux pour un marcheur bipède est mis en évidence en comparant les modèles $M_A$ et
$M_B$ de la [@tbl:results].

Les résultats expérimentaux montrent que, dans notre cas, ajouter des genoux à un simple compas divise environ le coût
de transport par deux, tout en augmentant la longueur optimale d’un pas. On note également que le coût additionnel en
termes de complexité et de temps de calcul est négligeable.

*NB:* Dans le cas d’un marcheur bipède réel, sans genoux, on ne peut marcher que sur un terrain parfaitement prévu
pour. Sans cela, la jambe qui se balance heurterait le sol au moment où l’angle entre les deux jambes s'annule.

#### Influence du torse

Dans ce cas, nous étudions l’impact de l’ajout d’un segment supérieur, correspondant au torse et à la tête rigidement
fixés l’un à l’autre et au bassin. Cette situation correspond aux modèles respectivement $M_A$ et $M_C$ de la
[@tbl:results], en ne considérant que l’actionnement actif.

On remarque donc que la modification d’un corps sans l’ajout de degré de liberté supplémentaire permet de réduire dans
ce cas le coût de transport de 40 %. Cela réduit également la longueur optimale du pas à 40 cm, ce qui est la borne
inférieure que nous avons autorisé.

Par ailleurs, le temps nécessaire à la convergence reste identique.

#### Influence du cou

Ici, nous considérons l’influence de l’actionnement du cou, en comparant les modèles $M_C$ et $M_D$ pour un même
actionnement.

Ces expériences nous montrent que l’accroissement du coût de transport entre ces deux cas est inférieur au pourcent,
alors que nous avons ajouté un actionneur et dépensons donc plus d’énergie. Cependant, le solveur a besoin d’un peu
plus de temps pour converger.

#### Comparaison des types d’actionnement

Cette comparaison considère seulement le modèle $M_C$, et étudie les différences entre un contrôleur idéal actif et un
contrôleur passif.

Si l’on compare les résultats des troisième et quatrième colonnes de la [@tbl:results], il apparaît que le coût de
transport, tel que nous le calculons à travers l’[@eq:cota], est supérieur pour le marcheur passif. Le temps de calcul
est lui inférieur dans le cas d’un actionnement de type Proportionnel Dérivé.

Cela peut être expliqué par la dimensionnalité du problème: dans le premier cas, le contrôleur est composé du nombre
de nœuds de multiple shooting de splines cubiques, tandis que dans le second cas il n’a que trois paramètres scalaires.
Il est donc plus complexe du point de vue du solveur, mais permet d’atteindre un meilleur résultat.

#### Passage à la troisième dimension

Notre méthode est générale et permet de considérer aussi bien des modèles 3D que des modèles 2D. Cependant, afin de
permettre au robot de garder son équilibre sur le lacet, nous lui avons ajouté des bras dans le modèle $M_E$.

En comparaison avec le modèle 2D sans bras $M_C$, le coût de transport est légèrement supérieur, mais reste inférieur à
celui du premier compas $M_A$. On remarque également que le temps de calcul et le nombre d’itérations du solveur sont
supérieurs, mais même dans ce cas complexe, l’efficacité de MUSCOD-II et celle de Pinocchio nous permettent de rester
sous la barre des dix secondes.
