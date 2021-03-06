### Trajectoires de nettoyage des bordures {#sec:bordures}

Dans un premier temps, une fois que la carte de la zone est disponible, nous souhaitons utiliser la brosse latérale
rétractable du robot afin de balayer le long des murs.

Dans cette section, nous expliquons comment nous détectons les segments de droites et les arcs de cercle dans cette
carte, afin de donner des consignes simples au robot.

L’objectif est de fournir la première partie de la `Roadmap` destinée au robot. Cette `Roadmap` sera dans un premier
temps composée d’une liste de segments définis par des paires $(q_s, q_e)$ indiquant les positions initiales et finales
nécessaires pour nettoyer chaque bordure.

#### Détection des segments de droites {#sec:borduresdroites}

L’obstacle le plus courant est un mur rectiligne. Il nous parait donc logique de commencer par chercher ce type
d’obstacle. Pour trouver la liste des `Pixels` de type `BOUNDARY` qui sont sur des segments de droite, nous utilisons
une transformée de Hough [@hough], décrite dans l’algorithme \ref{alg:hough} et illustrée dans la [@fig:hough].

\begin{algorithm}
\caption{Transformée de Hough}
\label{alg:hough}
\begin{algorithmic}[1]

\Procedure{HoughTransform}{$\texttt{BOUNDARY}, N_\rho, N_\theta$}

\State $\mathcal{H} \gets 0_{N_\rho, N_\theta}$
\Comment{Initialisation de la matrice $\mathcal{H}$}
\State $\pmb{\bar\theta} \gets \operatorname{linspace}(-\pi, \pi, N_\theta)$
\Commente{et des ensembles discretisés}
\State $\pmb{\bar\rho} \gets \operatorname{linspace}(0, \sqrt{x_{max}^2+y_{max}^2}, N_\rho)$
\Commente{de coordonées polaires.}

\For{$(x, y) \in \texttt{BOUNDARY}$}
\For{$\theta \in \pmb{\bar\theta}$}
\State $\rho \gets \arg\min\limits_{\rho \in \pmb{\bar\rho}}(|x \cos(\theta) + y \sin(\theta) - \rho|)$
\State $\mathcal{H}_{\rho,\theta} \gets \mathcal{H}_{\rho,\theta} + 1$
\Comment{Incrémentation du coefficient obtenu.}
\EndFor
\EndFor

\State \textbf{return} $\mathcal{H}$
\EndProcedure

\end{algorithmic}
\end{algorithm}

![Illustration graphique de la transformée de Hough. Dans l’image de droite, on voit trois points blancs, dont les
coordonnées correspondent aux paramètres $(\rho, \theta)$ des trois droites de l’image de
gauche.](imgs/hough.png){#fig:hough width=100%}

Cette transformée consiste à créer une matrice dite de Hough, $\mathcal{H}$, dont les dimensions sont la discretisation
souhaitée de l’espace en coordonnées polaires $(\rho, \theta)$: ($N_\rho, N_\theta$).

Ensuite, chaque point $(x, y)$ de l’ensemble `BOUNDARY` « vote » pour la liste des droites $(\rho, \theta)$ dont il
pourrait faire partie.

Le résultat de cette transformée de Hough est alors la matrice de Hough $\mathcal{H}$, dont les coefficients les plus
importants indiquent les paramètres des droites les plus probables.

Afin de détecter les trajectoires qui balaient les bordures, on utilise ensuite le cadre logiciel HPP pour simuler un
passage de ce robot suivant les droites fournies par la matrice de Hough dans les deux sens.

On garde alors les portions de ces trajectoires qui nettoient effectivement des `Pixels` de type `BOUNDARY` et qui ne
présentent pas de collisions entre le robot et son environnement.

Enfin, on enlève les `Pixels` ainsi nettoyés de l’ensemble de ceux de type `BOUNDARY` et on recommence autant de fois
que nécessaire.

L’extraction complète de ces trajectoires est explicitée dans l’algorithme \ref{alg:segments}, et dans
l’annexe [-@sec:annlemon], et illustrée dans la [@fig:borders].

\begin{algorithm}
\caption{Détection des segments de droite à balayer pour nettoyer le long des murs}
\label{alg:segments}
\begin{algorithmic}[1]

\While{$\texttt{BOUNDARY} \neq \varnothing$}
\For{$(\rho, \theta) \in \arg\max(\Call{HoughTransform}{\texttt{BOUNDARY}, N_\rho, N_\theta})$}
\State\Call{followLine}{$\rho, \theta, +1$}
\State\Call{followLine}{$\rho, \theta, -1$}
\EndFor
\EndWhile

\Procedure{followLine}{$\rho, \theta, \sigma$}
\State $start \gets false$
\For{$q \in \Call{line}{\rho, \theta, \sigma}$}
\Comment{\parbox[c]{.45\linewidth}{$\sigma$ est le sens de parcours à suivre. {\sc line} est explicité en
annexe~\ref{sec:annlemon}.}}
\State $valid \gets \Call{chkPos}{q}$
\Comment{\parbox[c]{.55\linewidth}{Place le robot pour que la brosse soit positionnée en $q$ et vérifie les
collisions et qu’on nettoie bien des \texttt{BOUNDARY}}}
\If{$valid \Ands \overline{start}$}
\State $start \gets true$
\State $q_s \gets q$
\Comment{Début d’une trajectoire}
\ElsIf{$start \Ands \overline{valid}$}
\State $start \gets false$
\State $\Call{addLane}{q_s, q}$
\Comment{\parbox[c]{.5\linewidth}{Ajoute la trajectoire à la \texttt{Roadmap} et supprime les \texttt{BOUNDARY}
nettoyées}}
\EndIf
\EndFor
\EndProcedure

\end{algorithmic}
\end{algorithm}

<div id="fig:borders">
![Détection des segments à balayer suivants une droite déterminée par transformée de Hough. On simule un balayage de
cette droite dans les deux sens, puis on ne garde que les portions qui nettoient des bordures et ne sont pas en
collision.](imgs/huit-abcd.png){height=5cm}
![Trajectoire complète de balayage des murs. Les segments des droites sont reliés entre eux par des trajectoires de
Reeds et Shepp, comme expliqué dans la [@sec:trajectoirefinale]](imgs/huit.png){height=5cm}

Illustration de la détection des segments de droites à balayer pour nettoyer le long des murs
</div>

\newpage

#### Détection des arcs de cercle {#sec:bordurescourbes}

Les environnements dans lesquels le robot LEMON est destiné à évoluer peuvent aussi comporter des obstacles
circulaires. Par exemple, une station de métro peut suivre une voie ferrée courbée. On peut également voir des piliers
ronds.

Ces arcs de cercle pourraient dans certains cas être approximés par des suites de segments, mais en pratique les
résultats n’étaient pas satisfaisants, comme le montre la [@fig:cercleko]. Nous avons donc ajouté à l’algorithme présenté
dans la section précédente une phase de transformée de Hough circulaire.

Un opérateur doit alors entrer la liste des rayons de cercles qui sont présent dans un environnement, et, pour chacun
de ces rayons, nous construisons une matrice de Hough dont les coefficients correspondent aux coordonnées $(x, y)$ du
centre d’un cercle d’un tel rayon à la place des coordonnées $(\rho, \theta)$ d’une droite.

<div id="fig:cercles">
![Suivi d’un cercle à partir de segments de droites.](imgs/cercle_ko.png){#fig:cercleko
height=3cm}
![Suivi d’un cercle par transformée de Hough circulaire.](imgs/cercle_ok.png){#fig:cercleok height=3cm}

Détection de cercles: transformées de Hough en $(\rho, \theta)$ à gauche et $(x, y, r)$ à droite.
</div>
