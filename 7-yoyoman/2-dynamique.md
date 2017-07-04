### Simulation Dynamique {#sec:yoyosimu}

Les marcheurs passifs sont des système intrinsèquement hybrides. Ils sont soumis à une dynamique continue lorsque la
jambe d’appui est en contact avec le sol, et ils sont également soumis à un impact lorque l’autre jambe heurte le sol.

Outre cette dynamique hybride, certaines contraintes de contact doivent être vérifiées pour assurer la fesabilité du
mouvement.

Dans cette section, nous décrivons les notations, le modèle paramétrique des marcheurs, et la formulation des contacts
utilisé dans notre système.

#### Notations

Nous assimilons le marcheur passif à un système dont la base flotte librement. On note son vecteur de configurations
par $\bm q \in SE(3) \mathbb{R}^n$, où $SE(3)$ est le groupe spécial Euclidien de dimension 3 exprimant la position de
la base du robot et $n$ le nombre de degrés de liberté (DoF). Les vitesses et accelerations de ce vecteur de
configurations sont notées respectivement $\dot{\bm q}$ et $\ddot{\bm q}$, et évoluent dans $\mathbb{R}^{6+n}$. Enfin,
le couple appliqué à chaque articulation est noté $\bm \tau \in \mathbb{R}^n$.

#### Modèle

Un marcheur passif est principalement un arbre cinématique, c’est à dire un arbre d’articulations où chaque
articulation a sa propre topologie (pivot, glissière, *etc.*) et un placement par rapport à l’articulation parente.
Les articulations sont les nœuds de l’arbre.

De plus, chaque articulation porte un corps, qui est défini par sa masse, la position de son centre de masse, et sa
matrice d’inertie. L’ensemble de ces corps définit la distribution des masses du modèle.

Cette structure en arbre et la distribution des masses correspondent aux paramètres structurels du système. Le modèle
du marcheur passif est donc paramétrisé par ces deux ensembles de paramètres:

$$ \text{model} (\textit{tree}, \textit{mass\_distribution}) $$

#### Contrôlleur

Une démarche est charactérisée par son controlleur qui est représenté par un ensemble de paramètres réels. Par exemple,
un controlleur peut être un ensemble de splines qui encodent les trajectoirs du couple, ou simplement les gains d’un
PID dans le cas d’un controlleur purement passif.

$$ \text{controller} (\textit{control\_parameters}) $$

#### Contacts

En ce qui concerne la dynamique continue, nous faisons l’hypothèse d’un contact ponctuel rigide avec des cônes de
frottement suivant les lois de Coulomb.

L’équation dynamique du système polyarticulé sous contraintes peut être définie comme dans l’[@eq:dyn].

$$ \begin{aligned}
    M(\bm q) \bm{\ddot q} + b(\bm q, \bm{\dot q}) &= S^\top \bm \tau + J_c(\bm q)^\top \bm f_c \\
    J_c(\bm q) \bm{\ddot q} + \dot J_c(\bm q, \bm{\dot q}) \bm{\dot q} &= 0
\end{aligned} $$ {#eq:dyn}

Dans l’[@eq:dyn], $M(\bm q)$ est la matrice d’inertie exprimée dans l’espace des articulations, $b(\bm q, \bm{\dot q})$
correspond aux effets de Coriolis, centrifuge et gravitationnel, $S$ est une matrice de sélection encodant la
sous-actuation, $J_c(\bm q)$ est la matrice Jacobienne des contacts avec $\bm f_c$ les forces aux contacts, et $.^\top$
est l’opérateur de transposition.

Une condition nécessaire et suffisante de contact sans glissement est que $\bm f_c$ reste à l’intérieur du cône de
friction $\mathcal{K}_c$. <!-- _w --> Cette condition implique que la composante normale de cette force de contact
reste positive (le sol ne peut pas tirer), et que la norme de sa composante tangeantielle et la norme du couple normal
sont limités par la composante normale.

Nous résolvons les deux équations de [@eq:dyn] ensemble, et ajoutons la contrainte du cône de friction directement dans
le problème de contrôle optimal pour assurer le modèle de contact de Coulomb [@brogliato99].

D’autres travaux ont essayé d’éliminer cet hypothèse supplémentaire [@stewart00], ce qui a amené des problèmes
d’optimisation de trajectoire [@tassa12;@posa14].

Dans le contexte de nos travaux, sélectionner à l’avance les phases de contacts n’est pas une limitation.

L’accélération des articulations et les forces aux contacts sont donc données dans l’[@eq:accf]

$$\begin{aligned}
    \bm{\ddot q} &= M^{-1}(I_n - J_c^t\Lambda_c^{-1}J_cM^{-1})(S^\top\bm\tau-\bm b) -
    M^{-1}J_c^\top\Lambda_c^{-1}\dot J_c\bm{\dot q} \\
    \bm f_c &=\Lambda_c^{-1}\left(J_cM^{-1}(\bm b-S^t\bm \tau)-\dot J_c \bm{\dot q}\right)
\end{aligned} $$ {#eq:accf}

Dans l’[@eq:accf], $\Lambda_c \triangleq J_cM^{-1}J_c^\top$ est la matrice d’inertie et $I_n$ la matrice identité de
dimension $n$. Les dépendances à $\bm q$ et $\bm{\dot q}$ ont été omises pour simplifier les notations.

#### Impacts

Les marcheurs passifs sont également soumis à des impacts. Dans ce cas, nous faisons l’hypothèse d’un impact instantané
et inélastique, avec un coefficient de restitution de zéro. En d’autres termes, la vitesse du point de contact après
l’impact est nulle.

La dynamique de l’impact nous conduit alors à une discontinuité dans l’espace des vitesses des articulations, ce qui
est décrit dans l’[@eq:impact].

$$\begin{aligned}
    \bm{\dot q^+} &= (I_n-M^{-1}J_c^\top\Lambda_c^{-1}J_c)\bm{\dot q^-} \\
    \bm\lambda_c &= \Lambda_c^{-1}J_c\bm{\dot q^-}
\end{aligned} $$ {#eq:impact}

Dans l’[@eq:impact], $\bm{\dot q^+}$ et $\bm{\dot q^-}$ sont les vitesses généralisées pré-impact et post-impact, et
$\bm\lambda_c$ est l’impulsion résultante de l’impact [@brogliato99].

D’autres modèles d’impact (*e.g.* élastique) pourraient également être introduits.

Ce modèle est fréquemment utilisé dans la littérature [@schultz10], même si sa consistence physique est contestée
[@chatterjee98].

#### Calcul Dynamique

Le solveur de contôle optimal doit calculer la dynamique du corps complet des milliers de fois lors de la procédure
d’intégration numérique. Dans ce but, nous avons utilisé Pinocchio [@pinocchioweb], une efficace librairie C++ qui sert
à modéliser et calculer les dynamiques directe et inverse d’un système polyarticulé en contact.

Pinocchio utilise la librairie C++ d’algère linéaire Eigen [@eigenweb].

Pinocchio est basée sur les algorithmes de Featherstone [@featherstone08], mais ils ont été implémentés de manière à
bénéficier de la prédiction de branche et des mécanismes de cache des processeurs modernes [@metapod].
