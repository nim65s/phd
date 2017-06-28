### Plannification de mouvement et contrôle {#sec:transplanif}

Dans cette section, nous explicitons la manière dont est générée le mouvement des plateformes robotiques supportant les
arbres.

Pour cela, nous commençons par la modélisation mathématique de la gestion des orientation et vitesses de traction des
tourelles, dans la [@sec:transmodel], puis nous voyons comment nous générons le mouvement à partir des sondes granier
dans la [@sec:transgene] et nous ajoutons certaines fonctions de lissage dans la [@sec:translissage].  Pour finir, nous
expliquons comment nous faisons en sorte que l’arbre *choisisse* sa destination, dans la [@sec:transgoal].

#### Modélisation de la plateforme {#sec:transmodel}

Comme nous l’avons vu dans la [@sec:transspecs] <!-- TODO: subsection & check qu’on l’a vu -->, l’artiste désire un
mouvement omnidirectionnel. Nous avons donc besoin de trois variables d’entrée, ce qui correspond à la classe de robot
mobile $(1, 2)$.

Puisque l’artiste désire que le robot n’aie pas une direction privilégiée du mouvement, nous choisissons un système de
coordonées polaires en $(v, \theta, \omega)$, où:

* $\theta \in [-\pi, \pi[$ est la direction dans laquelle se déplace le centre de l’AGV;
* $v \in [0, 1]$ est sa vitesse linéaire dans la direction $\theta$;
* $\omega \in [-1, 1]$ est sa vitesse angulaire.

Avec ce système de coordonées, on peu facilement calcure la sortie demandée par l’AGV, qui est la direction $\theta_i$
et la vitesse de traction $v_i$ de chaque roue $i$, comme le montre l’[@eq:agv]:

$$ \begin{aligned}
    v_{x_i} &= v \cos(\theta)- \omega R_i \sin(\alpha_i) \\
    v_{y_i} &= v \sin(\theta)+ \omega R_i \cos(\alpha_i) \\
    v_i &= \sqrt{v_{x_i}^2 + v_{y_i}^2} \\
    \theta_i &= \operatorname{atan2}(v_{y_i}, v_{x_i})
\end{aligned} $$ {#eq:agv}

Dans l’[@eq:agv], $(R_i, \alpha_i)$ est la position angulaire de la roue $i$, comme on peut le voir sur la
[@fig:octogons]

<div id="fig:octogons">
![De $(v, \theta, \omega)$ à $(v_i, \theta_i)$](tikz/octogon_1.pdf){#fig:octogon1}
![Construction géométrique](tikz/octogon_2.pdf){#fig:octogon2}

$(v_i, \theta_i)$ en fonction de $(v, \theta, \omega)$ et $(R_i, \alpha_i)$
</div>

Avec cette construction, on peut assurer l’unicité du centre instantanné de rotation, et que donc on ne risque pas de
se retrouver dans une situation ou les tourelles risquent d’écarteler un AGV, comme on peut le voir sur la
[@fig:octogon3]

![Centre Instantané de Rotation (CIR)](tikz/octogon_3.pdf){#fig:octogon3}

#### Génération de mouvement {#sec:transgene}

D’après les spécifications établies avec l’artiste, la génération du mouvement doit provenir du métabolisme de l’arbre.
Et comme nous venons de le voir, nous avons besoin de trois variables indépendantes d’entrée. Nous choisissons donc
d’utiliser les signaux de trois sondes Granier implantées à différents endroits de l’arbre, que nous notons $(s_1, s_2,
s_3)$ et normalisons dans $[0, 1]$.

Deux de ces sondes peuvent être directement connectées aux vitesses linéaire et angulaire du centre de l’AGV, comme on
peut le voir dans l’[@eq:speeds]:

$$ \begin{aligned}
    v &= s_1 \\
    \omega &= 2s_2 - 1
\end{aligned} $$ {#eq:speeds}

Les unités de ces vitesses sont ensuites déduites pour satisfaire les spécifications sur la vitesse générale de
l’arbre. Dans ce cas, la vitesse maximale du tronc de l’arbre est d’un mètre par minute (soit environ 17 milimètres par
seconde), mais les roues de l’AGV peuvent aller jusqu’à deux mètres par minute. Par conséquent, nous n’avons qu’à
multiplier chaque $v_i$ par 17mm/s avant de les envoyer à l’AGV.

Une stratégie globale de génération de mouvement a été établie avec l’artiste, et implique que l’arbre se *souvienne* à
quel endroit l’une des variables de son métabolisme était à son maximum ou son minimum. Un arbre ira donc
alternativement chercher le soleil et l’ombre, en fonction de ses sondes Granier, dans un lieu TODO

#### Lissage {#sec:translissage}

#### Sélection du but {#sec:transgoal}
