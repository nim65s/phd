### Trajectoires de nettoyage des bordures {#sec:bordures}

Dans un premier temps, une fois que la carte de la zone est disponible, nous souhaitons utiliser la brosse latérale
rétractable du robot afin de balayer le long des murs.

Dans cette section, nous expliquons comment nous détectons les segments de droites et les arcs de cercle dans cette
carte, afin de donner des consignes simples au robot.

#### Détection des segments de droites

L’obstacle le plus courant est un mur rectiligne. Il nous parait donc logique de commencer par chercher cet type
d’obstacle. Pour trouver la liste des `Pixels` de type `BOUNDARY` qui sont sur des segments de droite, nous utilisons
une transformée de Hough (alg. \ref{alg:hough}).

\begin{algorithm}
\caption{Transformée de Hough}
\label{alg:hough}
\begin{algorithmic}[1]

\Procedure{HoughTransform}{$\texttt{BOUNDARY}, n_\rho, n_\theta$}

\State $\mathcal{H} \gets 0_{n_\rho, n_\theta}$
\Comment{Initialisation de la matrice $\mathcal{H}$}
\State $\bar\theta \gets \operatorname{linspace}(-\pi, \pi, n_\theta)$
\Commente{et des ensembles discretisés}
\State $\bar\rho \gets \operatorname{linspace}(0, \sqrt{x_{max}^2+y_{max}^2}, n_\rho)$
\Commente{de coordonées polaires.}

\For{$(x, y) \in \texttt{BOUNDARY}$}
\For{$\theta \in \bar{\theta}$}
\State $\rho \gets \arg\min\limits_{\rho \in \bar\rho}(|x \cdot \cos(\theta) + y \cdot \sin(\theta) - \rho|)$
\State $\mathcal{H}_{\rho,\theta} \gets \mathcal{H}_{\rho,\theta} + 1$
\Comment{Incrémentation du coefficient obtenu.}
\EndFor
\EndFor

\State \textbf{return} $\mathcal{H}$
\EndProcedure

\end{algorithmic}
\end{algorithm}

Cette transformée consiste à créer une matrice dite de Hough, $\mathcal{H}$, dont les dimensions sont la discretisation
souhaitée de l’espace en coordonnées polaires $(\rho, \theta)$: ($n_\rho, n_\theta$).

Ensuite, chaque point $(x, y)$ de l’ensemble `BOUNDARY` « vote » pour la liste des droites $(\rho, \theta)$ dont il
pourrait faire partie.

Le résultat de cette transformée de Hough est alors la matrice de Hough $\mathcal{H}$, dont les coefficients les plus
importants indiquent les paramètres des droites les plus probables.

\newpage

Afin de détecter les trajectoires qui balaient les bordures, on utilise ensuite le cadre logiciel HPP pour simuler un
passage de ce robot suivant les droites fournies par la matrice de Hough dans les deux sens.

On garde alors les portions de ces trajectoires qui nettoient effectivement des `Pixels` de type `BOUNDARY` et qui ne
sont présentent pas de collisions entre le robot et son environnement.

Enfin, on enlève les `Pixels` ansis nettoyés de l’ensemble de ceux de type `BOUNDARY` et on recommence autant de fois
que nécessaire.

L’extraction complète de ces trajectoires est explicitée dans l’alg. \ref{alg:segments}.

\begin{algorithm}
\caption{Détection des segments de droite à balayer}
\label{alg:segments}
\begin{algorithmic}[1]

\While{$\texttt{BOUNDARY} \neq \varnothing$}
\For{$(\rho, \theta) \in \arg\max(\Call{HoughTransform}{\texttt{BOUNDARY}, n_\rho, n_\theta})$}
\For{$(x, y) \in droite(\rho, \theta)$}
\EndFor
\EndFor
\EndWhile
\end{algorithmic}
\end{algorithm}


<!--
   -\State $(x_s, y_s, x_e, y_e) \gets \Call{FindExtremities}{\rho, \theta}$
   -\Procedure{FindExtremities}{$\rho, \theta$}
   -
   -\If{$\sin(\theta) \simeq 0$}
   -\State $x_s, y_s \gets x_{min} + \rho, y_{min}$
   -\State $x_e, y_e \gets x_{min} + \rho, y_{max}$
   -\ElsIf{$\cos(\theta) \simeq 0$}
   -\State $x_s, y_s \gets x_{min}, y_{min} + \rho$
   -\State $x_e, y_e \gets x_{max}, y_{min} + \rho$
   -\Else
   -\State $x_a, y_a \gets x_{min}, y_{min} + \rho / \sin(\theta)$
   -\State $x_b, y_b \gets x_{min} + \rho / \cos(\theta), y_{min}$
   -\State $x_c, y_c \gets x_{max}, y_{min} + (\rho - (y_{max} - y_{min}) \cos(\theta) / \sin(\theta)$
   -\State $x_d, y_d \gets x_{min} + (\rho - (x_{max} - x_{min}) \sin(\theta) / \cos(\theta)), y_{max}$
   -\EndIf
   -
   -\State \textbf{return} $x_s, y_s, x_e, y_e$
   -\EndProcedure
   -->




#### Détection des arcs de cercle

pareil, mais avec des cercles de rayon donnés.

