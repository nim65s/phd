### Création de la carte {#sec:carto}

Dans cette section, nous partons d’un plan généré par les capteurs laser du robot, constitué d’une liste d’obstacles.

Afin de réaliser des tests de performances dans un maximum de cas, ce plan peut provenir de différentes sources :

- un fichier texte généré par le prototype de BA Robotic Systems composé de deux nombres par lignes indiquant les
  coordonnées de chaque point obstacle trouvé par les lasers;
- une image (par exemple un plan d’architecte) et une échelle;
- en utilisant directement l’API de la librairie implémentée pour l’occasion, par exemple dans un contexte de
  production sur le robot.

L’objectif est d’extraire la position des murs de ce nuage de point, afin de générer des trajectoires de balayage des
bords de ces murs. On a aussi besoin de pouvoir savoir où le robot peut passer ou non.

Pour cela, nous créons une classe `Bitmap` pour discrétiser la zone d’évolution. Ses bords sont ceux d’un rectangle
dont la largeur, la longueur et l’orientation sont calculées automatiquement pour englober la surface à nettoyer et
limiter la consommation en mémoire, et donc ainsi optimiser la vitesse d’exécution des algorithmes suivants.

Cette classe `Bitmap` est composée de `Pixels`, qui peuvent avoir plusieurs étiquettes:

- `OBSTACLE` si au moins un point obstacle est à l’intérieur;
- `FREE` sinon;
- `BOUNDARY` si c’est un `FREE` directement à côté d’un `OBSTACLE`;
- `REACHABLE` si c’est un `FREE` accessible au robot;
- `CLEANED` s’il est sur le chemin de balayage final.

D’autres `OBSTACLES` peuvent être ajoutés par un utilisateur pour définir des zones interdites circulaires ou
polygonales. On en ajoute également tout autour de l’aire définie par le `Bitmap`.

Les zones `REACHABLE` sont calculées à partir de la position de départ du robot, ainsi que de ses dimensions physiques.

Une zone de tests a été réalisée dans les locaux de BA Robotic Systems, et nous en avons créé une carte ([@fig:carte]).

Sur cette image, les `Pixels` en rouge contiennent des `OBSTACLES`, ceux en bleu sont des `BOUNDARY`, et ceux en verts
représentent les `FREE` dont l’intensité varie avec la distance aux `Pixels` de type `OBSTACLE`. Cette distance nous
permet de savoir où le robot peut passer ou non.

<!--TODO: developper, parler de voronoi, mettre une citation-->

![Exemple de carte créée avec la classe `Bitmap`.](imgs/carte.png){#fig:carte width=100%}
