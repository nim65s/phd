# Conclusion {-}

## Conclusion

Au cours de cette thèse, nous avons étudié la génération de mouvement ainsi que la planification de trajectoire pour la
locomotion de différents types de robots mobiles et bipèdes.

Ce chapitre de conclusion récapitule nos contributions à la maîtrise de ces modes de locomotion, et présente diverses
perspectives.

### Robotique mobile

Dans la partie [-@sec:mobile], nous avons utilisé trois classes de robots mobiles:

- des robots différentiels de classe $(2, 0)$, dans le chapitre [-@sec:offroad];
- des robots à tourelle de classe $(1, 1)$, dans le chapitre [-@sec:lemon];
- des robots tri-tourelles de classe $(1, 2)$, dans le chapitre [-@sec:transhumus].

Il en ressort que des robots différentiels sont bien plus facile à maîtriser que des robots *car-like*. En effet, ces
deux classes de robots ont le même nombre de degrés de manœuvrabilité, mais la première a deux degrés mobilité alors
que la seconde n’en a qu’un, compensé par un dégré de dirigeabilité.

Cela a notamment engendré des complications lors de la mise en œuvre des trajectoires que nous générons sur le
prototype développé par BA Robotics Systems, et particulièrement au niveau des points de rebroussement. Pour un robot
de classe $(1, 1)$, il est nécessaire de s’arrêter à chaque point de rebroussement pendant la durée nécessaire à la
modification du degré de dirigeabilité.

Ensuite, en comparant les robots mobiles omnidirectionnels avec des robots ne pouvant pas se déplacer latéralement, il
apparaît que ce gain implique un grand coût de complexité, tant sur le design mécanique du robot que sur les
algorithmes de contrôle. En effet, à moins d’utiliser des roues omnidirectionnelles ([@fig:omniwheel]), le robot a
forcément plus d’actionneurs que de degrés de liberté. Les algorithmes de contrôle doivent donc s’assurer que les
degrés de liberté supplémentaires soient correctement asservis par rapport aux actionneurs principaux.

![Une roue omnidirectionnelle. Ce mécanisme est rarement fabriqué pour des robots de plusieurs tonnes, mais il aurait
en théorie grandement facilité le contrôle bas niveau des robots du projet
*transhumus*.](imgs/omniwheel.jpg){#fig:omniwheel height=4cm}

#### Contributions

Pour les projets *offroad* et *transhumus*, vus dans les chapitres [-@sec:offroad;-@sec:transhumus], nous avons créé
des mouvements répondant principalement à des contraintes esthétiques. Ces mouvements sont générés par des variables
extérieures, telles que la force et la direction du vent ou la vitesse de flux de sève. Ces générations de mouvement
assurent également des contraintes de couverture de surface et d’évitement d’obstacles connus *a priori*.

Pour le projet LEMON vu dans le chapitre [-@sec:lemon], nous avons généré des trajectoires de suivi des murs et de
balayage des surfaces, utilisant une carte créée à l’aide de techniques de SLAM, et essayant de minimiser le nombre de
manœuvres à effectuer.

#### Perspectives

Les trois projets vus dans cette première partie ont tous été réalisés en un temps extrêmement court suivant les
contraintes opérationnelles.

Les deux projets artistiques sont suffisament aboutis sur le plan théorique, et ont prouvé qu’ils ont pu fonctionner
pendant la durée de leurs expositions respectives. Cependant, une réécriture de certaines parties du code utilisé ainsi
qu’un plus grand nombre de tests et de gestion d’erreurs rendraient ces œuvres plus faciles à installer, plus
maintenables, et plus pérennes.

Aussi, pour ces deux projets, il serait particulièrement utile d’améliorer le système de géolocalisation, par exemple
en recoupant les données issues de technologies différentes (vision, laser, ondes UWB, odométrie, ultrasons, etc.).

Concernant le projet LEMON, des perspectives ont déjà été évoquées dans la [@sec:lemonfutur]. Cependant, à la lumière
de notre comparaison entre différentes classes de robots, il apparaît que pour cette application, utiliser un robot
différentiel permettrait de résoudre les problèmes de suivi des trajectoires que nous générons, de même que de les
parcourir en un temps réduit, puisqu’il ne serait plus nécessaire de s’arrêter pour manœuvrer à chaque point de
rebroussement.

### Robotique Humanoïde

Dans la partie [-@sec:humanoide], nous avons étudié la génération de mouvements pour différents marcheurs bipèdes.

#### Contributions

Nous avons pour cela créé et prototypé une méthode de codesign de marcheurs bipèdes utilisant la librairie de calculs
dynamique Pinocchio et le solveur de contrôle optimal MUSCOD-II.

Nous avons ensuite testé ce prototype logiciel et montré qu’il peut servir à comparer différentes architectures de
chaînes polyarticulées, différentes méthodes d’actionnement, et optimiser différents critères.

#### Perspectives

Nous avons vu le potentiel de notre méthode, et il reste donc naturellement à l’utiliser dans des cas concrets, par
exemple pour choisir le type d’actionnement d’un robot particulier, ou de générer différentes trajectoires de marche
suivant une liste pré-définie de critères à optimiser, ou encore d’optimiser le design mécanique lors de la création
d’un nouveau robot.

Outre les questions relatives à la gestion d’autres types d’actionneurs, de pieds ellipsoïdaux, de la stabilité, ainsi
qu’au choix d’une fonction de coût vues dans la [@sec:perspectives], il serait également intéressant d’essayer
d’utiliser un solveur de contrôle optimal libre. En effet, MUSCOD-II est un excellent logiciel, mais sa licence fermée
nous empêche actuellement de mieux diffuser notre méthode et de la rendre accessible au plus grand nombre.
