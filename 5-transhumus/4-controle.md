### Planification de mouvement et contrôle {#sec:transplanif}

Dans cette section, nous explicitons la manière dont est généré le mouvement des plate-formes robotiques supportant les
arbres.

Pour cela, nous commençons par la modélisation mathématique de la gestion des orientations et vitesses de traction des
tourelles, dans la [@sec:transmodel], puis nous voyons comment nous générons le mouvement à partir des sondes Granier
dans la [@sec:transgene] et nous ajoutons certaines fonctions de lissage dans la [@sec:translissage].  Pour finir, nous
expliquons comment nous faisons en sorte que l’arbre « choisisse » sa destination, dans la [@sec:transgoal].

#### Modélisation de la plate-forme {#sec:transmodel}

Comme nous l’avons vu dans la [@sec:transspecs], l’artiste désire un mouvement omnidirectionnel. Nous avons donc besoin
de trois variables d’entrée, ce qui correspond à la classe de robot mobile $(1, 2)$.

Puisque l’artiste désire que le robot n’ait pas une direction privilégiée du mouvement, nous choisissons un système de
coordonnées polaires en $(v, \theta, \omega)$, où:

* $\theta \in [-\pi, \pi[$ est la direction dans laquelle se déplace le centre de l’AGV;
* $v \in [0, 1]$ est sa vitesse linéaire dans la direction $\theta$;
* $\omega \in [-1, 1]$ est sa vitesse angulaire.

Avec ce système de coordonnées, on peut facilement calculer la sortie demandée par l’AGV, qui est la direction $\theta_i$
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

Avec cette construction, on peut assurer l’unicité du centre instantané de rotation, et que donc on ne risque pas de
se retrouver dans une situation ou les tourelles risquent d’écarteler un AGV, comme on peut le voir sur la
[@fig:octogon3]

![Centre Instantané de Rotation (CIR)](tikz/octogon_3.pdf){#fig:octogon3}

\newpage

#### Génération de mouvement {#sec:transgene}

D’après les spécifications établies avec l’artiste, la génération du mouvement doit provenir du métabolisme de l’arbre.
Et comme nous venons de le voir, nous avons besoin de trois variables indépendantes d’entrée. Nous choisissons donc
d’utiliser les signaux de trois sondes Granier implantées à différents endroits de l’arbre, que nous notons $(s_1, s_2,
s_3)$ et normalisons dans $[0, 1]$.

Deux de ces sondes peuvent être directement connectées aux vitesses linéaires et angulaires du centre de l’AGV, comme
on peut le voir dans l’[@eq:speeds]:

$$ \begin{aligned}
    v &= s_1 \\
    \omega &= 2s_2 - 1
\end{aligned} $$ {#eq:speeds}

Les unités de ces vitesses sont ensuite déduites pour satisfaire les spécifications sur la vitesse générale de
l’arbre. Dans ce cas, la vitesse maximale du tronc de l’arbre est d’un mètre par minute (soit environ 17 millimètres par
seconde), mais les roues de l’AGV peuvent aller jusqu’à deux mètres par minute. Par conséquent, nous n’avons qu’à
multiplier chaque $v_i$ par 17mm/s avant de les envoyer à l’AGV.

Une stratégie globale de génération de mouvement a été établie avec l’artiste, et implique que l’arbre se « souvienne »
à quel endroit l’une des variables de son métabolisme était à son maximum ou son minimum. Un arbre ira donc
alternativement chercher le soleil et l’ombre, en fonction de ses sondes Granier, dans un lieu où il se souvient de
l’état de son flux de sève, ou dans un lieu où il n’est pas encore allé.

La principale composante de la génération de trajectoire est donc le paramètre $\theta$. La géolocalisation donne la
position et l’orientation absolue $(x, y, \alpha)$ de l’AGV, donc une fois que la destination $(x_{goal}, y_{goal})$
est déterminée grâce à la dernière sonde Granier, on peut obtenir ce paramètre $\theta$ suivant l’[@eq:theta].

$$
\theta = \left(\operatorname{atan2}\left(y - y_{goal}(s_3), x - x_{goal}(s_3)\right) - \alpha\right) \% 2 \pi - \pi
$$ {#eq:theta}

Ce principe règle le problème de couverture de l’espace et est développé dans la [@sec:transgoal].

#### Lissage {#sec:translissage}

Au-dessus de ce principe basique de génération de mouvement, nous implémentons un composant de lissage qui
contrôle la vitesse angulaire maximale de chaque roue. En effet, les deux AGVs qui évoluent sur l’esplanade peuvent
facilement s’embourber, et notamment en tournant leurs roues trop brutalement, creusant ainsi le sol sous leurs roues.

De son côté, l’AGV à l’intérieur du pavillon français peut produire un bruit strident fort désagréable lorsque son pneu
crisse sur le béton, toujours s’il tourne trop vite.

Si ce composant détecte que la différence entre la direction d’un AGV et la direction du $goal$ est supérieure à
$2\pi/3$, il peut également inverser le sens de rotation des roues pour n’avoir à tourner que de moins de $\pi/3$. Ceci
améliore notamment le comportement aux points de rebroussement, lorsque l’AGV change de $goal$.

Un composant similaire est implémenté sur l’AGV au niveau de chaque tourelle, tout en s’assurant que le centre
instantané de rotation reste unique.

#### Sélection du but {#sec:transgoal}

La génération de mouvement définit comment un AGV évoluerait seul sur un plan infini. Nous avons ajouté certaines règles
pour nous assurer que la sélection du $goal$ ne fera pas aller un AGV dans un mur ou un autre AGV. Ces règles sont
détaillées dans l’algorithme \ref{alg:goal}, mais l’idée générale est de mettre à jour en continu deux cartes de l’aire
d’évolution avec le $timestamp$ et $s_3$ dans la case correspondant aux coordonnées actuelles.

\begin{algorithm}
\caption{Génération de mouvement et de trajectoire}
\label{alg:goal}
\begin{algorithmic}[1]

\Loop
    \State \emph{start\_loop}:
    \Comment{Label du début}
    \State $map_{sap flow}[position] \gets s_3$
    \Comment{Mise à jour de cartes}
    \State $map_{timestamp}[position] \gets timestamp$
    \If {$\Vert goal - position\Vert < 1$}
        \Comment{Besoin d’un nouveau $goal$}
        \For {$try \gets 1, N$}
            \If {$state = 1$}
                \State $goal \gets \arg\min(map_{sap flow})$
            \ElsIf {state = 2}
                \State $goal \gets \arg\max(map_{sap flow})$
            \Else
                \State $goal \gets \arg\min(map_{timestamp})$
            \EndIf
            \State $state \gets (state + 1) \% 3$
            \If {$(goal - position) \cap (borders \cup {trajectory}_{other AGV}) = \varnothing$}
                \State \textbf{goto} \emph{continue}
                \Comment{Pas d’obstacle entre $position$ et $goal$}
            \EndIf
        \EndFor
        \State $goal \gets position$
        \Comment{Échec de recherche d’un nouveau $goal$}
        \State $v \gets 0$
        \State $\omega \gets s_2$
        \Comment{L’arbre peut continuer de tourner sur place}
        \State sleep 10s
        \State \textbf{goto} \emph{start\_loop}
        \Comment{Nouvelle tentative}
    \EndIf
    \State \emph{continue}:
    \Comment{Label de succès}
    \State $v \gets s_1$
    \State $\omega \gets s_2$
    \Comment{Voir \ref{sec:transgene}}
    \State $\theta_{goal} \gets \left(\operatorname{atan2}\left(y - y_{goal}(s_3), x - x_{goal}(s_3)\right) -
    \alpha\right) \% 2 \pi - \pi$
    \State sleep 1s
\EndLoop

\end{algorithmic}
\end{algorithm}

De cette manière, nous obtenons des cartes $map_{sapflow}$ et $map_{timestamp}$ indiquant les zones où la sève a coulée
rapidement ou non (qui coïncideront probablement avec les zones d’ombre et de soleil), et les zones où un AGV n’est pas
allé depuis longtemps.

Ensuite, une machine d’états finis alterne le $goal$ entre des endroits où $s_3$ était maximum, puis minimum, puis un
endroit où l’arbre n’est pas allé depuis longtemps.

Dans certaines circonstances, il est possible qu’aucune de ces zones ne soit atteignable en ligne droite, sans traverser
de bordure, ou de trajectoire d’un autre AGV. Dans un tel cas de *deadlock*, l’AGV doit simplement attendre dans sa
position courante.

Les traces générées par cet algorithme en simulation sont données dans la [@fig:ressimulation].

Un des objectifs de la génération de trajectoire est d’assurer une couverture raisonnable des zones d’évolution
intérieure et extérieure. De multiples essais en simulation ([@sec:simulateur]) nous ont permis de régler
précisément les contrôles à travers la normalisation des paramètres $(s_1, s_2, s_3)$.

Dans la zone extérieure, la synchronisation des arbres est effectuée de manière centralisée, à partir de leur
localisation respective. Du point de vue formel, ce système ne garantit pas l’absence de minima locaux. Pour autant, la
complétion de cet algorithme n’est pas un problème du point de vue pratique.

En effet, deux personnes de l’équipe du pavillon sont tout le temps présentes sur le site pour éviter tout problème.
Ces personnes ont la possibilité de déverrouiller un *deadlock* en donnant artificiellement aux arbres un nouveau
$goal$.

En pratique, les interventions de l’équipe arrivent rarement (moins d’une fois par semaine, pendant la période
nominale). Par ailleurs, un tel *deadlock* est impossible pour l’arbre dans le pavillon, puisqu’il évolue seul et
dans une zone convexe.

![Exemple de couverture d’espace en simulation. Sur site, un tel test aurait demandé plusieurs jours entre la fin de
l’installation matérielle et l’ouverture de la Biennale.](imgs/covering.png){#fig:ressimulation width=100%}

\newpage
