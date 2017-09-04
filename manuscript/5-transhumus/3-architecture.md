### Architecture logicielle {#sec:transarchi}

> Designing a robot architecture is much more of an art than a science.
> \par\raggedleft--- *Handbook of Robotics*, @handbook

Dans la section précédente, nous avons détaillé notre choix de fournisseurs de solutions matérielles. Nous étions
également en charge de la gestion des principaux développements logiciels. La [@fig:soft] récapitule les différents
composants du système et les flux de données entre eux.

![Architecture logicielle: chaque arbre a trois sondes Granier qui sont utilisées par le planificateur de trajectoire.
Le planificateur de trajectoire récupère également la position et l’orientation actuelle de chaque robot grâce au
système de géolocalisation, puis calcule les vitesses de traction et d’orientation de chaque tourelle de chaque AGV. Un
utilisateur peut aussi directement donner des consignes au planificateur de trajectoire lorsque c’est nécessaire. Les
variables $(s_1, s_2, s_3)$, $(x, y, \alpha)$ et $(v_i, \theta_i)$ sont explicitées dans la
[@sec:transplanif].](tikz/schema_block.pdf){#fig:soft width=100%}

Les logiciels ont été développés pour être le plus modulaire possible. Il est donc facile de passer des cas de tests
en simulation aux cas de production. Cette modularité permet également de surmonter la diversité de technologies
utilisées par nos fournisseurs, puisque des convertisseurs sont simples et rapide à coder.

En effet, les sondes Granier fournissent des valeurs toutes les 30 secondes sur une liaison série, le logiciel des
AGV attend des commandes ASCII sur un socket TCP, et la suite logicielle de géolocalisation est bâtie sur une
technologie .NET qui ne peut être étendue que via des modules d’un cadre logiciel propriétaire dont la fréquence
d’actualisation peut aller de 1 à 100 hertz.

Par conséquent, nous avons utilisé une architecture logicielle fondée sur la librairie de messagerie ZeroMQ
[@zeromq], qui peut être utile pour tous nos canaux de communication. Cette librairie est disponible dans plusieurs
langages de programmation, et fournit une abstraction aux problématiques de connections / déconnections des sockets
sous-jacentes. Enfin, elle implémente des schémas de communication classiques tels que *Client/Server*,
*Publish/Subscribe* (*PUB/SUB*) et *PUSH/PULL*.

L’idée générale de notre architecture est d’avoir un planificateur de trajectoire qui est un composant central, et qui
est capable d’effectuer des *Pull* depuis les entrées et des *Publish* vers les sorties. Ainsi les autres composants
peuvent se mettre à récupérer des données via des *Subscribe* et en envoyer grâce à des *Push* à tout moment, sans
perturber le processus principal. Certaines fonctionnalités périphériques peuvent également être ajoutées à la volée en
étant à la fois un *Subscriber* et un *Pusher*. Cette architecture est plus précisément détaillée dans l’annexe
[-@sec:anntranshumus].

Une interface utilisateur graphique fondée sur des technologies web a également été développée pour aider l’équipe du
pavillon à voir la situation actuelle, et gérer les éventuels problèmes qui pourraient survenir
([@fig:simulateur-right]).

![Exemple d’utilisation de l’interface utilisateur web, affichant la situation actuelle: deux AGVs se déplacent sur
l’esplanade, et on peut voir leur position et orientation, ainsi que l’orientation et la vitesse de traction des
tourelles.](imgs/simulateur-right.png){#fig:simulateur-right width=100%}

Dans des cas plus complexes, ceci nous permet également de travailler sur l’installation à
distance, pour éviter d’avoir besoin d’ingénieurs sur place. Enfin, pendant la période de développement, cette
interface a également permis à l’artiste de se faire une idée du mouvement des arbres au fur et à mesure de notre
avancement.

*NB:* En temps normal, cette interface utilisateur est inutile, vu que le système est entièrement autonome.
