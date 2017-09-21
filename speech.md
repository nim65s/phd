# 1

Bonjour, merci d’être venus à la soutenance de ma thèse, portant sur la génération de mouvement en robotique mobile et
humanoïde.

# 2

La robotique consiste à créer des machines universelles, dans le sens où elles peuvent éxécuter une large variété de
tâches, y compris certaines qui n’étaient pas prévues au moment de la conception.

Pour cela, un robot a besoin d’être capable de générer des mouvements, que ce soit de manipulation ou de locomotion.
Dans cette thèse, nous avons étudié deux modes de locomotion terrestre: le roulement sans glissements chez les robots
mobiles, et la marche chez les robots humanoïdes.

# 3

Commençons par les robots à roues.

# 4

En fonction des types de roues utilisées pour construire un robot, celui-ci a un degré de mobilité, compris
entre 1 et 3, correspondant au nombre de degrés de libertés pouvant être directement actionés.

Il a également un degré de dirigeabilité, compris entre 0 et 2, correspondant au nombre de roues pouvant être
indépendamment réorientées afin de diriger le robot.

La somme de ces deux nombres correspond donc au degré de manœuvrabilité, c’est à dire le nombre total de degrés de
libertés sur lesquels le robot peut agir.

On montre qu’il existe alors cinq classes de robots mobiles en fonction de ces degrés.

Ainsi, les mouvements de locomotion qu’il est possible de générer sur un robot dépendent directement de cette classe.

Dans la suite de cette partie, nous allons étudier plus particulièrement 3 de ces classes, à commencer par les robots
de classe (2, 0), plus connus sous le nom de robots différentiels, pouvant donc actionner directement deux degrés de
liberté. Ensuite, nous remplaceront un degré de mobilité par un degré de dirigeablilité, et verrons la classe (1, 1),
et les robots pouvant se déplacer comme des voitures.
Pour finir, nous ajouterons un second degré de dirigeabilité pour la classe (1, 2) afin d’étudier les robots
omnidirectionels.

: (2, 0), (1, 1), et (1, 2).

# 5

Dans ce chapitre, nous allons voir un projet réalisé préalablement à cette thèse, introduisant diverses
problématiques similaires à celles qui seront traitées par la suite, et nous étudierons les robots différentiels, de
classe (2, 0).

# 6

Ces robots différentiels sont principalement composés de deux roues co-axiales indépendemment motorisées. une troisième
roue, pouvant par exemple être de type caster, sert uniquement à gérer l’équilibre du robot.

# -

On peut donc contrôler indépendemment leurs vitesse linéaire et angulaire, en agissant simplement sur la somme et la
différence des vitesses de rotation des moteurs.

# 7

Nous allons maintenant voir un projet mettant en œuvre trois de ces robots.

Céleste Boursier-Mougenot est un artiste installationiste français qui a été exposé au musée des abattoirs de Toulouse
de janvier à mai 2014. Pour cette exposition, il a créé une œuvre intitulée *offroad*, dont voici le cahier des
charges.

Trois pianos à queue doivent se mouvoir dans une salle. Cela implique donc de modifier ces pianos de manière à
motoriser les roues se trouvant de part et d’autre du clavier. La troisième roue est quand-à-elle laissée libre.

Ces pianos évolueront au milieu du public, ce qui pose d’évidentes contraintes de sécurité.

Ils peuvent se rentrer dedans et dans les murs, de manière à faire résonner leur table d’harmonies afin de créer une
musique vivante.

Et enfin, leurs mouvements doivent être qualifiables de naturels, plutôt que de robotiques. En d’autres termes,
l’artiste doit valider l’esthétisme des mouvements générés par les pianos robots.

# 8

Afin de réaliser cette dernière contrainte, nous avons implémenté la méthode des champs de potentiels. Ainsi, en
positionnant dynamiquement à divers endroits de l’aire d’évolution des pianos des potentiels attractifs ou répulsifs,
chaque piano se déplace comme s’il glissait sur des pentes entre des creux et des bosses.

Des vitesses linéaire et angulaires à appliquer aux pianos à un instant donné est donc donné directement par
différences finies du champ de ces potentiels suivant leurs axes longitudinaux et latéraux.

Il ne reste donc plus qu’à définir comment sont créés les divers potentiels.

Pour cela, l’artiste ne veut pas que son œuvre repose sur un générateur de nombres aléatoires informatiques.

# 9

Nous avons donc utilisé comme entrée du système une girouette et un anémomètre. Ainsi, la vitesse, l’accélération et la
direction du vent ont servi à moduler la position et l’amplitude des différents potentiels imposés  sur les pianos.

Nous avons également positionné des potentiels répulsifs le long des murs de la salle pour ne pas que les pianos les
heurtent trop violement. De la même manière, après un choc entre pianos, ceux-ci deviennent des potentiels répulsifs
les uns pour les autres afin de pouvoir se dégager du lieu de la collision.

Enfin, un visiteur peut être détecté par le système, et agir comme un potentiel attractif ou répulsif.

# 10

Pour que ce système de génération de mouvements puisse fonctionner, il est nécessaire de géolocaliser les pianos. Nous
avons pour cela décidé de positioner des caméras au plafond et d’utiliser des algorithmes de détection des contours.

Cependant, comme vous pouvez le voir sur cette figure, les pianos ont une teinte en une texture proches de ceux du
sols. Les algorithmes classiques de détection des contours se sont donc révélés insuffisants.

Nous avons donc du améliorer ce système de géolocalisation en inférant la position des pianos à un instant donné en
fonction de l’état précédent.


# 11

Sur ces vidéos, vous pouvez voir la vue du public en vitesse réelle à gauche, et la vue depuis le plafond en time lapse
à droite. Vous pouvez donc apprécier les mouvements générés par ces pianos transformés en robots différentiels, mais
également les réactions variées du public face à cette œuvre.

# 12

Dans le chapitre suivant, nous allons passer de robots de classe (2, 0) à des robots de classes (1, 1). Ces robots ont
le même degrés de manœuvrabilité et peuvent donc suivre les mêmes trajectoires que des robots différentiels.

Cependant, puisque nous avons remplacé un degré de mobilité par un degré de dirigeabilité, ce qui implique qu’il
devient nécessaire de réorienter une roue afin de pouvoir agir sur le second degré de liberté de ces robots qui se
comportent comme des voitures.

# 13

Pour réaliser techniquement un tel robot, on peut par exemple utiliser une tourelle comportant une roue motorisée
montée sur un axe orientable. Deux roues fixes sont ajoutées pour l’équilibre du robot.

# 14

Nous allons maintenant voir un projet mettant en œuvre un tel robot.

Ce robot est le LEMON, et a été dévellopé par la société BA Robotics Systems Group dans le but d’automatiser une
autolaveuse autoportée, dans des environnements tels que des quais de gare ou des hopitaux.

Pour pouvoir nettoyer le sol, ce robot commence par cartographier son environnement en utilisant des techniques de
SLAM.

Une fois que c’est fait, il doit balayer le long des murs, et enfin nettoyer les surfaces.

Cette fois, la principale contrainte sur la génération de mouvement n’est plus du domaine de l’artistique, mais de
celui de l’efficacité. Le robot doit donc minimiser son nombre de manœuvres, à la fois dans le but de ne pas faire de
traces au sol, mais aussi dans celui de nettoyer un endroit donné en un temps relativement court.

# 15

Nous commençons donc par construire une carte discrétisée de la zone à nettoyer, en nottant tous les obstacles détectés
par le SLAM, ainsi que des polygones et des cercles entrés par un opérateur. Cela correspond aux pixels rouges sur la
figure.

À partir de ces obstacles, nous construisons un diagramme de Voronoï à partir de la position initiale du robot, afin de
détecter où il peut passer ou non, ainsi que les pixels correspondants aux bordures des obstacles, qui sont ici en bleu.

# 16

Ensuite, à l’aide d’une transformée de hough, on cherche les paramètres des droites formées par les pixels de bordures.
Puis on simule le nettoyage de ces droites par la brosse latérale du robot dans les deux sens, et on ne garde que les
portions qui balayent effectivement des bordures et qui ne sont pas en collision.

# -

On relie ensuite ces segments de droite de proche en proche par des trajectoires de reeds and shepp. Pour cela, on
utilise un algorithme glouton, et en lui indiquant la distance de reeds and shepp entre la configuration finale d’un
segment et la configuration initiale des autres.

Lors de ces transitions, la brosse latérale du robot servant à balayer les bordures est rentrée.

# 17

Les trajectoires de Reeds and Shepp étant obtenues à l’aide de méthodes aléatoires, les transitions dans les angles ne
sont jamais optimales, et peuvent parfois être plutôt mauvaises.

# -

Nous faisons donc le choix de relacher la contraintes de couverture d’espace, et raccourcissons les segments des
droites à balayer afin d’essayer de connecter ces segments par des trajectoires de Dubins, qui sont optimales pour des
robots mobiles de classe (1, 1) se déplaçant uniquement en marche avant.

# 18

Une fois que les bordures sont balayées, il reste à nettoyer les surfaces. Pour cela, nous prenons la direction du plus
grand segment de droite trouvé par la transformée de hough effectuée précédement, et nous quadrillons les espaces qui
n’ont pas encore été balayés.

De la même manière, un algorithme glouton cherche à relier les segments de droites trouvés, sauf que cette fois-ci les
segments peuvent être parcourus dans un sens ou dans l’autre.

# 19

Demo

# 20

# 21

# 22

# 23

# 24

# 25

# 26

# 27

# 28

# 29

# 30

# 31

# 32

# 33

# 34

# 35

# 36

# 37

# 38

# 39

# 40

# 41

# 42

# 43

# 44

# 45

# 46

