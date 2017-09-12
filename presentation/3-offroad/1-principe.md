#### Fonctionnement

Commençons par étudier les robots mobiles les plus simples: les robots différentiels.
Ces robots ont principalement deux roues parallèles dont la vitesse est commandée indépendamment.

![Exemple de robot mobile différentiel](tikz/differentiel.pdf){height=2cm}

. . .

On peut donc contrôler indépendemment leurs vitesse linéaire et angulaire.

$$
\begin{aligned}
v      &= \cfrac{\omega_r + \omega_l}{2} \cdot r \\
\omega &= \cfrac{\omega_r - \omega_l}{l} \cdot r
\end{aligned}
$$

