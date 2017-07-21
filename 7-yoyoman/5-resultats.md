### Résultats des premiers tests {#sec:restest}

\newcolumntype{C}{>{\centering\arraybackslash}m{.12\linewidth}}
\newcolumntype{Y}{>{\centering\arraybackslash}X}

\begin{table*}
    \normalsize\medskip\noindent
    \begin{tabularx}{\textwidth}{l| *{6}{Y}}
        \toprule \multicolumn{7}{l}{{\underline{\textbf{\textsc{Entrées}}}}}
        \\ &
        \multicolumn{1}{Y}{\includegraphics{tikz/compass}} &
        \multicolumn{1}{Y}{\includegraphics{tikz/knees}} &
        \multicolumn{2}{c}{\includegraphics{tikz/compass_bust}} &
        \includegraphics{tikz/compass_neck} &
        \includegraphics{tikz/arms}
        \\ Modèle & $M_A$ & $M_B$ & \multicolumn{2}{c}{$M_C$} & $M_D$ & $M_E$
        \\ Description & Compas & $M_A$ avec des genous &
        \multicolumn{2}{c}{$M_A$ avec un buste} &
        \multicolumn{1}{Y}{$M_C$ avec un cou} &
        \multicolumn{1}{Y}{$M_C$ avec des bras}
        \\  \rowcolor{gray!20}
        Masse totale & 33.1\,kg & 33.1\,kg & 60.3\,kg & 60.3\,kg & 60.3\,kg & 65.9\,kg
        \\ Actionnement & actif & actif & actif & \textbf{passif} & actif & actif
        \\  \rowcolor{gray!20}
        Dimension & 2D & 2D & 2D & 2D & 2D & \textbf{3D}
        \\ \midrule \multicolumn{7}{l}{{\underline{\textbf{\textsc{Sorties}}}}}
        \\ &
        \includegraphics[height=4cm]{imgs/2_100_fixed.png} &
        \includegraphics[height=4cm]{imgs/2_100_fixed_kneeled.png} &
        \includegraphics[height=4cm]{imgs/2_100_fixed_with_bust.png} &
        \includegraphics[height=4cm]{imgs/2_100_fixed_passive.png} &
        \includegraphics[height=4cm]{imgs/2_100_fixed_with_neck.png} &
        \includegraphics[height=4cm]{imgs/2_100_fixed_3d.png}
        \\ \rowcolor{gray!20}
        CoT & 0.1007 & 0.0544 & 0.0618 & 0.2796 & 0.0621 & 0.0651
        \\ Longueur & 0.56\,m & 0.85\,m & 0.40\,m & 0.40\,m & 0.40\,m & 0.41\,m
        \\ \rowcolor{gray!20}
        Vitesse &  0.70\,m/s & 1.06\,m/s & 0.50\,m/s & 0.50\,m/s & 0.50\,m/s & 0.51\,m/s
        \\ \midrule \multicolumn{7}{l}{{\underline{\textbf{\textsc{Performances}}}}}
        \\ Itérations & 56 & 40 & 76 & 9 & 66 & 108
        \\ \rowcolor{gray!20}
        Durée & 2.8\,s & 2.9\,s & 2.6\,s & 1.2\,s & 4.1\,s & 7.6\,s
        \\ \bottomrule
    \end{tabularx}
    \caption{Six marcheurs bipèdes sont comparés afin de déterminer l’influence des genous, du buste, du cou, des bras,
    et du type d’actionnement. Pour chaque exemple, l’algorithme nous fourni la démarche, le coût final de transport
    optimisé et la longueur d’un pas. Les deux dernières lignes donnent les performances de l’algorithme. Dans tous ces
    exemples, la durée d’un pas est fixée à 0.8 secondes et la pente du sol à 0.05 radians.}
    \label{tbl:results}
\end{table*}


Dans cette section, nous examinons les résultats des six expériences présentées dans la [@tbl:results] sous forme de
cinq comparaisons. Ces résultats sont également disponibles en vidéo[^11].

[^11]: [https://hal.archives-ouvertes.fr/hal-01360450v2/file/3D.mp4](https://hal.archives-ouvertes.fr/hal-01360450v2/file/3D.mp4)

<!--TODO: fichier hal.laas.fr, v2-->

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

#### Influence du buste

Dans ce cas, nous étudions l’impact de l’ajout d’un segment supérieur, correspondant au torse et à la tête rigidement
fixés l’un à l’autre et au bassin. Cette situation correspond aux modèles respectivement $M_A$ et $M_C$ de la
[@tbl:results], en ne considérant que l’actionnement actif.

On remarque que la modification d’un corps sans l’ajout de degré de liberté supplémentaire permet de réduire dans
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
celui du premier compas $M_A$.

On remarque également que le temps de calcul et le nombre d’itérations du solveur sont supérieurs, mais même dans ce
cas complexe, l’efficacité de MUSCOD-II et celle de Pinocchio nous permettent de rester sous la barre des dix
secondes.
