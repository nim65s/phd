### Planification {#sec:planification}

Une fois que l’on connait à un instant donné la position $(x, y, \alpha)$ d’un piano et qu’on est capable de le
déplacer en utilisant $(v, \omega)$, le robot est contrôlable ; mais il reste à planifier, à plus haut niveau, ce que
l’on veut que le robot fasse.

Naturellement, c’est à Céleste Boursier-Mougenot qu’il revient de décider ce que les robots doivent faire. Mais bien
sûr, c’était à nous, roboticiens, d’implémenter techniquement le comportement choisi.

L’un des principaux challenges de ce projet a donc été d’arriver à nous comprendre, artiste et roboticiens, sur les
spécifications. Cela a donc également été l’un des éléments les plus riches de cette collaboration.

Dans un premier temps, l’artiste nous a expliqué qu’il ne souhaitait pas voir de mouvements « robotiques ». Nous avons
donc évité de donner aux pianos des suites de consignes simples, comme avancer et reculer en ligne droite, et tourner
sur place, en suivant une machine à états classique.

Nous avons donc tenté d’implémenter des trajectoires plus « douces », telles que des splines. Cependant, des problèmes
de nécessité de prédiction ainsi que de deadlocks non triviaux se sont rapidement posés, et les délais semblaient bien
trop court pour que nous puissions finaliser l’implémentation d’une telle solution à temps pour le vernissage.

De plus, dans tous les cas, Céleste Boursier-Mougenot n’était pas satisfait par le rendu artistique de nos premières
itérations.

#### Champs de potentiel {#sec:potentiels}

La solution aux problèmes évoqués ci-dessus a été d’utiliser la méthode des champs de potentiel. Dans ce paradigme, on
considère que l’aire d’évolution des pianos est parsemée de potentiels $P_i$ caractérisés par une localisation, une
norme $\|P_i\|$, et un signe $s_i$, suivant si l’on désire un potentiel attractif ou un potentiel répulsif.

On calcule alors en un point $p$ l’action de ce champ de potentiels $C(p)$ suivant l’[@eq:sumpot].

$$ C(p) = \sum_i \cfrac{s_i \|P_i\|}{\mathrm{dist}(P_i, p) + 1} $$ {#eq:sumpot}

La [@fig:surface] montre un exemple de ce qu’il se passe si l’on trace sur un graphe 3D l’allure de cette fonction dans
l’aire d’évolution des pianos. Il suffit alors d’imaginer une telle surface comme un relief dans lequel le piano
se baladerait en se déplaçant suivant les pentes.

![Champs de potentiels](imgs/surface.png){#fig:surface width=60%}

Il n’est donc plus nécessaire de prédire la trajectoire des pianos, et en cas de deadlock il suffit d’ajouter un fort
potentiel répulsif sur le piano. De plus, le mouvement produit semble « naturel » et non « robotique » pour un artiste,
ce qui n’est pas une contrainte simple à remplir en utilisant d’autres méthodes.

Par différences finies, on peut donc déterminer la forme de la « pente » sur laquelle roule un piano, et donc ajuster
sa vitesse en conséquence, comme le montre l’[@eq:pots].

$$ \begin{aligned}
v &= \cfrac{C(O + \varepsilon \vec{x}) - C(O - \varepsilon \vec{x})}{2\varepsilon} K_v \\
\omega &= \cfrac{C(O + \varepsilon \vec{y}) - C(O - \varepsilon \vec{y})}{2\varepsilon} K_{\omega_{}}
\end{aligned} $$ {#eq:pots}

Dans notre cas, nous avons considéré les murs et d’autres zones interdites comme des potentiels répulsifs constants.
En jouant sur la norme du potentiel des murs, on peut modifier la fréquence à laquelle les pianos vont s’y cogner. On
peut alors contenter à la fois l’artiste qui désire que cela puisse arriver, et l’équipe du musée qui doit maintenir
les murs dans un état correct[^4].

[^4]: Un rideau de scène de 8.30 × 13.25m réalisé par Pablo Picasso se trouve en permanence derrière l’une de ces
cloisons.  On comprendra donc que l’équipe du musée tienne à ce que la cloison ne s’effondre pas.

Ensuite, les pianos sont vus les uns par les autres comme des potentiels, tantôt attractifs tantôt répulsifs, jusqu’à
ce que l’on détecte un choc. À ce moment-là, les pianos deviennent de forts potentiels répulsifs l’un pour l’autre pour
une durée limitée.

Enfin, selon les circonstances, le système de planification peut repérer un visiteur (toujours grâce aux caméras
présentes au plafond), et le considérer comme un potentiel attractif ou répulsif.

#### Entrée du système

Comme nous l’avons vu dans la [@sec:potentiels], il suffit d’ajouter des potentiels pour que les pianos bougent.
Cependant, Céleste Boursier-Mougenot souhaite que le comportement de ses œuvres ne soit ni prédictible, ni dicté par
un générateur de nombres aléatoires.

Ainsi, dans les œuvres décrites dans la [@fig:perturbations], des éléments extérieurs comme les particules cosmiques,
les résultats en temps réel de Google News ou encore les chaînes de télévision sont introduits et dirigent l’expérience
du visiteur.

Dans *offroad*, l’artiste a choisi d’utiliser le vent. Nous avons donc installé une girouette et un anémomètre sur un
mur extérieur du musée, de sorte qu’ils soient visibles à travers des fenêtres lorsqu’on est à côté de l’œuvre.

La vitesse du vent, son accélération, et sa direction sont donc dans cette œuvre les principaux facteurs qui créent
des potentiels, soit directement, soit indirectement en désignant un visiteur. Celui-ci peut ainsi, sans le savoir,
faire partie de la performance.
