### Simulation Dynamique {#sec:yoyosimu}

Les marcheurs bipèdes sont des systèmes intrinsèquement hybrides [@grizzle10]. Ils sont soumis à une dynamique continue
lorsque la jambe d’appui est en contact avec le sol, puis ils sont ensuite soumis à un impact lorsque l’autre jambe
heurte le sol.

Outre cette dynamique hybride, certaines contraintes de contact doivent être vérifiées pour assurer la faisabilité du
mouvement.

Dans cette section, nous décrivons les notations, le modèle paramétrique des marcheurs, et la formulation des contacts
utilisé dans notre système.

#### Notations

Nous assimilons le marcheur bipède à une chaîne polyarticulée dont la base flotte librement. On note son vecteur de
configurations par $\pmb q \in SE(3) \times \mathbb{R}^n$, où $SE(3)$ est le groupe spécial Euclidien de dimension 3
exprimant la position de la base du robot, et $n$ le nombre de degrés de liberté (DoF). Les vitesses et accélérations
de ce vecteur de configurations sont notées respectivement $\dot{\pmb q}$ et $\ddot{\pmb q}$, et évoluent dans
$\mathbb{R}^{6+n}$. Enfin, le couple appliqué à chaque articulation est noté $\pmb \tau \in \mathbb{R}^n$.

#### Modèle

Un marcheur bipède est principalement un arbre cinématique, c’est-à-dire un arbre d’articulations où chaque
articulation a sa propre topologie (pivot, glissière, *etc.*) et un placement par rapport à l’articulation parente.
Les articulations sont les nœuds de l’arbre.

De plus, chaque articulation porte un corps, qui est défini par sa masse, la position de son centre de masse, et sa
matrice d’inertie. L’ensemble de ces corps définit la distribution des masses du modèle.

Cette structure en arbre et la distribution des masses correspondent aux paramètres structurels du système. Le modèle
du marcheur bipède est donc paramétré par ces deux ensembles de paramètres:

$$ \text{modèle} (\textit{arbre}, \textit{distribution\_masses}) $$

#### Contrôleur

Une démarche est caractérisée par son contrôleur qui est représenté par un ensemble de paramètres réels. Par exemple,
un contrôleur peut être un ensemble de splines qui encodent les trajectoires du couple, ou simplement les gains d’un
PID dans le cas d’un contrôleur purement passif.

$$ \text{contrôleur} (\textit{paramètres\_contrôle}) $$

#### Contacts {#sec:contcont}

En ce qui concerne la dynamique continue, nous faisons l’hypothèse d’un contact ponctuel rigide avec des cônes de
frottement suivant les lois de Coulomb.

L’équation dynamique du système polyarticulé sous contraintes peut être définie comme dans l’[@eq:dyn].

$$ \begin{aligned}
    M(\pmb q) \pmb{\ddot q} + b(\pmb q, \pmb{\dot q}) &= S^\top \pmb \tau + J_c(\pmb q)^\top \pmb f_c \\
    J_c(\pmb q) \pmb{\ddot q} + \dot J_c(\pmb q, \pmb{\dot q}) \pmb{\dot q} &= 0
\end{aligned} $$ {#eq:dyn}

Dans l’[@eq:dyn], $M(\pmb q)$ est la matrice d’inertie exprimée dans l’espace des articulations, $b(\pmb q,
\pmb{\dot q})$
correspond aux effets de Coriolis, centrifuge et gravitationnel, $S$ est une matrice de sélection encodant la
sous-actuation, $J_c(\pmb q)$ est la matrice Jacobienne des contacts avec $\pmb f_c$ les forces aux contacts, et $.^\top$
est l’opérateur de transposition.

Une condition nécessaire et suffisante de contact sans glissement est que $\pmb f_c$ reste à l’intérieur du cône de
frottements $\mathcal{K}_c$. <!-- _w --> Cette condition implique que la composante normale de cette force de contact
reste positive (le sol ne peut pas tirer), et que la norme de sa composante tangentielle et la norme du couple normal
sont limités par la composante normale.

Nous résolvons les deux équations de [@eq:dyn] ensemble, et ajoutons la contrainte du cône de frottements directement
dans le problème de contrôle optimal pour assurer le modèle de contact de Coulomb [@brogliato99].

D’autres travaux ont essayé d’éliminer cet hypothèse supplémentaire [@stewart00], ce qui a amené des problèmes
d’optimisation de trajectoire [@tassa12;@posa14].

Dans le contexte de nos travaux, sélectionner à l’avance les phases de contacts n’est pas une limitation.

L’accélération des articulations et les forces aux contacts sont donc données dans l’[@eq:accf]

$$\begin{aligned}
    \pmb{\ddot q} &= M^{-1}(I_n - J_c^t\Lambda_c^{-1}J_cM^{-1})(S^\top\pmb\tau-\pmb b) -
    M^{-1}J_c^\top\Lambda_c^{-1}\dot J_c\pmb{\dot q} \\
    \pmb f_c &=\Lambda_c^{-1}\left(J_cM^{-1}(\pmb b-S^t\pmb \tau)-\dot J_c \pmb{\dot q}\right)
\end{aligned} $$ {#eq:accf}

Dans l’[@eq:accf], $\Lambda_c \triangleq J_cM^{-1}J_c^\top$ est la matrice d’inertie et $I_n$ la matrice identité de
dimension $n$. Les dépendances à $\pmb q$ et $\pmb{\dot q}$ ont été omises pour simplifier les notations.

#### Impacts

Les marcheurs bipèdes sont également soumis à des impacts. Dans ce cas, nous faisons l’hypothèse d’un impact instantané
et inélastique, avec un coefficient de restitution de zéro. En d’autres termes, la vitesse du point de contact après
l’impact est nulle.

La dynamique de l’impact nous conduit alors à une discontinuité dans l’espace des vitesses des articulations, ce qui
est décrit dans l’[@eq:impact].

$$\begin{aligned}
    \pmb{\dot q^+} &= (I_n-M^{-1}J_c^\top\Lambda_c^{-1}J_c)\pmb{\dot q^-} \\
    \pmb\lambda_c &= \Lambda_c^{-1}J_c\pmb{\dot q^-}
\end{aligned} $$ {#eq:impact}

Dans l’[@eq:impact], $\pmb{\dot q^+}$ et $\pmb{\dot q^-}$ sont les vitesses généralisées pré-impact et post-impact, et
$\pmb\lambda_c$ est l’impulsion résultante de l’impact [@brogliato99].

D’autres modèles d’impact (*e.g.* élastique) pourraient également être introduits.

Ce modèle est fréquemment utilisé dans la littérature [@schultz10], même si sa consistance physique est contestée
[@chatterjee98].

#### Calcul Dynamique

Le solveur de contrôle optimal doit calculer la dynamique du corps complet des milliers de fois lors de la procédure
d’intégration numérique. Dans ce but, nous avons utilisé Pinocchio [@pinocchioweb], une librairie C++ efficace qui sert
à modéliser et calculer les dynamiques directe et inverse d’un système polyarticulé en contact.

Pinocchio utilise la librairie C++ d'algèbre linéaire Eigen [@eigenweb].

Pinocchio est basé sur les algorithmes de @featherstone08, mais ils ont été implémentés de manière à
bénéficier de la prédiction de branche et des mécanismes de cache des processeurs modernes [@metapod].
