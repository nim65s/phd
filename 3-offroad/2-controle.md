### Contrôle

À son plus bas niveau, le contrôle du déplacement d’un robot nécessite à minima des capteurs lui permettant de savoir
quelle est sa position à un instant donné, et des actionneurs lui permettant de se déplacer. Ces deux composants
doivent ensuite être reliés par un mécanisme de décisionnel.

Dans cette section, nous verrons quelles solutions techniques ont été mises en œuvre dans le cadre de ce projet pour
ces besoins de perception et d’action dans les [@sec:perception;@sec:action], puis, dans la section suivante,
[-@sec:planification], quel mécanisme décisionnel a été utilisé.

#### Perception {#sec:perception}

Lorsqu’on évoque la perception, l’être humain pense à ses capteurs internes qui constituent ses cinq sens.
Pourtant, en robotique, il est souvent plus aisé d’utiliser des capteurs qui ne sont pas embarqués dans le robot.

Ainsi, pour de la géolocalisation de pianos à queue en intérieur pour *off road*, la plupart des solutions techniques
que nous avons envisagées, comprenant celle que nous avons retenue, consistaient à équiper l’aire d’évolution des
pianos plutôt que les pianos eux-mêmes.

En effet, dans une pièce connue, l’une des meilleures solutions pour déterminer où un robot se situe et dans quelle
orientation il est par rapport à son environnement est d’utiliser un télémètre laser balayant un plan horizontal. En ne
gardant que les points les plus éloignés, on trouve la position des murs, et détermine donc la position et
l’orientation du laser, et donc du robot, aux éventuelles symétries de la salle près. Mais cette solution était
largement en dehors de nos moyens financiers.

Une seconde solution, au coût financier négligeable, et à la simplicité et rapidité de mise en place appréciable, est
l’odométrie. Elle consiste à ajouter un capteur sur l’axe des roues afin de déterminer incrémentalement la position à
chaque instant. Cependant, la précision de cette méthode s’amenuise au cours du temps, et n’est donc pas adaptée à un
système devant pouvoir fonctionner pendant une journée complète sans intervention humaine. De plus, cette solution ne
fonctionne pas si la roue dérape ou saute. Dans notre cas, un choc entre deux pianos semble suffisamment important pour
justifier que l’on n’utilise pas cette technique.

Parmi les solutions externes de géolocalisation, il existe également la triangulation et/ou trilatération à base
d’ondes (dans le domaine visible, auditif, WiFi, Bluetooth, *etc.*). Cette solution, bien qu’efficace (*cf.*
[@sec:transloc]), n’est pas simple à mettre en place, et faute de temps et d’argent nous avons du l’abandonner.

Notre choix s’est donc porté sur l’installation de caméras au plafond de la pièce, et l’utilisation du traitement de
ces images pour détecter la position et l’orientation des trois pianos. Cette solution a entre autres l’avantage d’être
plutôt discrète, et également de nous permettre de détecter les visiteurs si besoin (*cf.* [@sec:potentiels]).

La première étape est alors de fusionner les images des différentes caméras, comme le montre la [@fig:merged].

![Images des caméras au plafond superposées au niveau de l’altitude des pianos.](imgs/merged.jpg){#fig:merged
height=9cm}

Malheureusement, la mise en œuvre de cette solution retenue ne s’est pas révélée aussi simple que prévu. En effet, dans
notre cas, la texture du sol était similaire à celle des pianos, et le contraste entre leurs teintes n’était pas
suffisant, donc sous un éclairage uniforme, les images présentaient un grain similaire pour les pianos et le sol, comme
en témoigne la [@fig:extraction].

![Image des caméras à gauche, sortie de l’algorithme d’extraction de contours pour cette image à
droite. Les contours des machines sont bien visibles, mais ceux des pianos sont
estompés par endroits, y compris pour l’œil humain.](imgs/pbvision.jpg){#fig:extraction height=5cm}

Heureusement, en connaissant la position des pianos à un instant $t$ et leur vitesse approximative, il est possible de
forcer l’algorithme d’extraction des contours à chercher un contour particulier (connu) dans un zone réduite à
l’instant $t + \delta t$.

En pratique, cela a fonctionné, mais a nécessité l’ajout d’une interface utilisateur pour que les opérateurs (les
guides et vigiles du musée) positionnent correctement des masques sur les pianos le matin en démarrant l’installation.


#### Action {#sec:action}

Pour faire bouger ces pianos, deux moteurs ont été ajoutés et couplés via une chaîne aux roues qui sont de part et
d’autre du clavier. La troisième roue, au bout de la queue, de type caster, n’est pas modifiée. Le piano devient ainsi
un robot mobile différentiel de type (2, 0) ([@fig:piano]).

![Les pianos sont désormais des robots mobiles différentiel (2, 0)](tikz/piano.pdf){#fig:piano height=6cm}

Sa vitesse linéaire $v$ est donc proportionnelle à la moyenne des vitesses des moteurs, et sa vitesse angulaire
$\omega$ est proportionnelle à la différence des vitesses de ses moteurs, comme le montre l’[@eq:differentiel].

$$
\begin{aligned}
v &= \cfrac{\omega_r + \omega_l}{2} \cdot r \\
\omega &= (\omega_r - \omega_l) \cdot r
\end{aligned}
$$ {#eq:differentiel}

où $r$ est le rayon des roues du piano, et $\omega_r$ et $\omega_l$ respectivement les vitesses appliquées aux roues
droite et gauche.

L’[@eq:differentiel] est vraie pour le point $O$ du piano se trouvant au milieu du clavier, donc tout point
$P$ du piano a une vitesse $\|v_P\| = v + \omega \cdot \| OP \|$.

On comprend donc que, lorsque le piano tourne, l’extrémité de sa queue atteint rapidement une vitesse conséquente. Ce
fait n’est pas une problématique à négliger lorsque la tête d’un enfant visiteur pourrait se trouver au point
d’intersection des trajectoires de deux pianos.
