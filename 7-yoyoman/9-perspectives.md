### Perspectives {#sec:perspectives}

Dans les sections [-@sec:tete] et [-@sec:proto], nous avons brièvement mentionné les principaux travaux en cours au
moment de la rédaction de cette thèse. Dans cette section, nous énumérons les différents points encore en suspens.

#### Actionneurs

L’étude des actionneurs comprenant des ressorts réalisée dans la [@sec:sea] ouvre diverses pistes pour des travaux
futurs. Par exemple, on pourrait envisager d’utiliser des actionneurs combinant un ressort en série et un autre en
parallèle (SE+PEA), ou encore des actionneurs à impédance variable (VSA).

On pourrait aussi chercher à optimiser le type d’actionneur à utiliser en fonction de chaque articulation, étant donné
les différences entre leurs besoins.  Ainsi, en pratique, il n’est pas forcément utile d’avoir un actionneur complexe,
donc lourd et onéreux au niveau des épaules, si notre seul objectif est la locomotion. Ces paramètres peuvent aisément
être ajoutés dans la fonction de coût.

La marche n’est pas non plus le seul mode de locomotion bipède[^14], il serait donc possible de chercher à
étudier dans notre modèle l’intérêt de ces actionneurs pour la course ou le saut [@grimmer12].

[^14]: Sans compter les nombreux modes de locomotion multipèdes, que nous n’avons pour l’instant pas l’intention de
traiter.

Par ailleurs, il pourrait être intéressant de prendre en compte des modèles plus réaliste d’actionneurs, notamment
dans le cas où ceux-ci sont capables de fonctionner également en générateur de courant. Par exemple les actionneurs
« proprioceptifs » du robot Cheetah [@wensing17] sont particulièrement performants pour absorber les chocs, notamment
grâce à leur rétroactivité.

Cela nous permettrait ainsi de pouvoir utiliser une fonction de coût représentant plus fidèlement la consommation
énergétique réelle du robot.


#### Pieds ellipsoïdaux

@carpentier15 ont proposé une formulation analytique de contacts de roulement sans glissement qui est compatible avec
la formulation dynamique présentée en [@sec:contcont]. L’ajout de ce modèle de contacts à notre méthode pourrait
grandement améliorer la qualité des mouvements générés ainsi que nous permettre de gérer des scenario plus complexes.

Comme nous l’avons vu dans la [@sec:proto], nous avons pour objectif d’utiliser des pieds ronds pour notre premier
prototype, en suivant @wisse07denise. L’ajout de cette formulation dans notre programme est donc l’une de nos
priorités.

#### Stabilité

Pour l’instant, notre méthode produit une trajectoire de référence cyclique encodant un régime permanent de marche.
Rien n’est prévu au cours de l’optimisation pour garantir la stabilité, et nous ne pouvons donc que la vérifier a
posteriori.

L’étude de la stabilité d’un marcheur oscillant autour d’un cycle limite est généralement effectuée par une observation
de la section de Poincaré [@grizzle10]. @benallegue13meta reprennent cette méthode et proposent comme mesure
l’espérance du nombre de pas qu’un robot en boucle ouverte peut faire avant de tomber (MFPT). Cette métrique pourrait
être directement inclue dans notre fonction de coût.

Outre l’étude d’un terrain ayant une texture présentée par @benallegue13meta, il est aussi possible de rechercher la
hauteur maximale d’une marche inattendue que le robot pourrait descendre sans tomber [@wisse07]. Cette métrique a
l’avantage d’être bien plus parlante, mais son calcul est plus complexe à mettre en œuvre dans le cadre de notre
méthode.

Une autre méthode classique utilise une analyse de Monte-Carlo. Elle est bien plus simple à mettre en place, mais
risque de faire exploser les temps de calculs au vu des dimensions du problème que l’on traite.

Il est également envisageable de poser un second problème d’optimisation au-dessus de l’actuel, visant à optimiser la
stabilité du contrôle en boucle ouverte [@mombaur01].

Enfin, une solution plus complexe sur le plan théorique et encore peu explorée serait d’utiliser des techniques de
contrôle optimal afin de générer un contrôleur en boucle ouverte de référence, puis d’extraire ce contrôleur pour le
réutiliser dans un contexte de contrôle rétroactif. Le contrôle rétroactif est déjà largement répandu dans le cadre de
la locomotion bipède [@westervelt07], et permet d’assurer la stabilité de la marche dans des conditions bien plus
vastes.

#### Fonctions de coût

Le choix d’une fonction de coût reste un problème ouvert, alors même qu’il est l’une des questions les plus importantes
en contrôle optimal.

Comme nous l’avons fait dans les travaux présentés dans la [-@sec:sea], on peut trouver dans la littérature différents
résultats en fonction de différentes fonctions de coût [@chevallereau01], ou des indications sur le choix de ces
fonctions de coût [@tassa12].

Tout au long de ce chapitre, nous avons évoqué diverses métriques qu’il serait judicieux d’ajouter dans cette fonction
de coût. Cependant, il n’est pas aisé d’arriver à faire convenablement cohabiter plusieurs termes au sein d’une
telle fonction. Pour cela, un paramètre de poids peut être utilisé comme dans l’[@eq:tete], mais il parait plus
raisonnable d’établir une hiérarchie dans les objectifs à la manière de @geisert17.
