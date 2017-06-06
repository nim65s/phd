### Contrôle

À son plus bas niveau, le contrôle de la locomotion d’un robot nécessite à minima des capteurs lui permettant de savoir
quelle est sa position à un instant donné, et des actionneurs lui permettant de se déplacer. Dans cette section, nous
verrons quelles solutions techniques ont été mises en œuvre dans le cadre de ce projet pour ces besoins respectivement
dans les [@sec:perception;@sec:action].

#### Perception {#sec:perception}

Lorsqu’on évoque la perception, l’être humain pense à ses capteurs intéroceptifs qui constituent ses cinq sens.
Pourtant, en robotique, il est souvent plus aisé d’utiliser des capteurs qui ne sont pas embarqués dans le robot.

Ainsi, pour de la géolocalisation de pianos à queue en intérieur pour *off road*, la plupart des solutions techniques
que nous avons envisagé, comprenant celle que nous avons retenue, consistaient à équiper l’aire d’évolution des pianos
plutôt que les pianos eux-même.

En effet, dans une pièce connue, l’une des meilleures solutions pour déterminer où un robot se situe et dans quelle
orientation il est utilise un télémètre laser balayant un plan horizontal. En ne gardant que les points les plus
éloignés, on détermine immédiatement la position et l’orientation du laser, et donc du robot, aux éventuelles
symmétries de la salle près. Mais cette solution était largement en dehors de nos moyens financiers.

Une seconde solution, au coût financier négligeable, et à la simplicité et rapidité de mise en place appréciable, est
l’odométrie. Elle consiste à ajouter un capteur sur l’axe des roues afin de déterminer incrémentalement la position à
chaque instant. Cependant, la précision de cette méthode s’amenuise au cours du temps, et n’est donc pas adaptée à un
système devant pouvoir fonctionner pendant une journée complète sans intervention humaine. De plus, cette solution ne
fonctionne pas si la roue dérape ou saute. Dans notre cas, un choc entre deux pianos semble suffisant important pour
justifier que l’on n’utilise pas cette technique.

Parmis les solutions extéroceptives de géolocalisation, il existe également la triangulation et/ou trilatération à base
d’ondes électro-magnétiques (WiFi, Bluetooth, ou autre). Cette solution, bien qu’efficace (*cf.*
[@sec:geolocalisation]), n’est pas simple à mettre en place, et faute de temps et d’argent nous avons du l’abandonner.

Notre choix s’est donc porté sur l’installation de caméras au plafond de la pièce, et l’utilisation du traitement de
ces images pour détecter la position et l’orientation des trois pianos. La première étape est alors de fusionner les
images des différentes caméras, comme le montre la figure [-@fig:merged].

\newpage

![Images des caméras au plafond superposées au niveau de l’altitude des pianos.](imgs/merged.jpg){#fig:merged width=46%}

Cependant, la mise en œuvre de cette solution retenue ne s’est pas révélée aussi simple que prévu. En effet, dans notre
cas, la texture du sol était similaire à celle des pianos, et le contraste entre leurs teintes n’était pas suffisant,
donc sous un éclairage uniforme, les images présentaient un grain similaire pour les pianos et le sol, comme en
témoigne la [@fig:extraction].

![Image des caméras à gauche, sortie de l’algorithme d’extraction de contours pour cette image à
droite. Les contours des machines sont bien visibles, mais ceux des pianos sont
estompés par endroits, y compris pour l’œil humain.](imgs/pbvision.jpg){#fig:extraction width=95%}

Heureusement, en connaissant la position des pianos à un instant $t$ et leur vitesse approximative, il est possible de
forcer l’algorithme d’extraction des countours à chercher un countour particulier (connu) dans un zone réduite à
l’instant $t + \delta t$.

En pratique, cela a fonctionné, mais a nécessité l’ajout d’une interface utilisateur pour que les opérateurs (les
guides et vigiles du musée) positionnent correctement des masques sur les pianos le matin en démarrant l’installation.


#### Action {#sec:action}

Pour faire bouger ces pianos, deux moteurs ont été ajoutés et couplés via une chaîne aux roues qui sont de part et
d’autre du clavier. La troisième roue, au bout de la queue, de type caster, n’est pas modifiée. Le piano devient ainsi
un robot mobile différentiel de type (2, 0) ([@fig:actdiff]).

![Les pianos sont désormais des robots mobiles différentiel (2, 0)](tikz/actdiff.pdf){#fig:actdiff width=33%}

Sa vitesse linéaire $v$ est donc proportionelle à la moyenne des vitesses des moteurs, et sa vitesse angulaire $\omega$
est proportionelle à la différence des vitesse de ses moteurs, comme le montre les équations suivantes:

\begin{align}
v &= \cfrac{\omega_r + \omega_l}{2} \cdot r \\
\omega &= (\omega_r - \omega_l) \cdot r
\end{align}

où $r$ est le rayon des roues du piano, et $\omega_r$ et $\omega_l$ respectivement les vitesses appliquées aux roues
droite et gauche.
