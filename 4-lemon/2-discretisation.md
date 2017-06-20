### Création de la carte {#sec:carto}

Dans cette section, nous partons d’un plan généré par les capteurs laser du robot, constitué d’une liste d’obstacles.

Afin de réaliser des tests de performances dans un maximum de cas, ce plan peut provenir de différentes sources :

- un fichier texte généré par le prototype de BA Système composé de deux nombres par lignes indiquant les coordonnées de
  chaque point obstacle trouvé par les lasers,
- une image (par exemple un plan d’architecte) et une échelle,
- en utilisant directement l’API de la librairie implémentée pour l’occasion.

L’objectif est d’extraire la position des murs de ce nuage de point, afin de générer des trajectoires de balayage des
bords de ces murs. On a aussi besoin de pouvoir savoir où le robot peut passer ou non.

Pour cela, nous créons une classe `Bitmap` pour discretiser la zone d’évolution. Ces bords sont ceux d’un rectangle
dont la largeur, la longueur et l’orientation sont calculées automatiquement pour englober la surface à nettoyer et
limiter la consommation en mémoire, et donc ainsi optimiser la vitesse d’éxecution des algorithmes.

Cette classe `Bitmap` est composée de `Pixels`, qui peuvent avoir plusieurs états:

- `OBSTACLE` si au moins un point obstacle est à l’intérieur,
- `FREE` sinon,
- `BOUNDARY` si c’est un `FREE` directement à côté d’un `OBSTACLE`,
- `REACHABLE` si c’est un `FREE` accessible au robot,
- `CLEANED` s’il est sur le chemin de balayage final.

Les zones `REACHABLE` sont calculées à partir des dimensions physiques du robot ainsi que sa position de départ.

D’autres `OBSTACLES` peuvent être ajoutés par un utilisateur pour définir des zones interdites circulaires ou
polygonales. On en ajoute également tout autour de l’aire définie par le `Bitmap`.

Une zone de tests a été réalisée dans les locaux de BA Systèmes, et nous en avons crée une carte ([@fig:carte]).

Sur cette image, les `Pixels` en rouge contiennent des obstacles, ceux en bleu sont des `BOUNDARY`, et ceux en verts
représentent les `FREE` dont l’intensité varie avec la distance aux `OBSTACLE`. Cette distance nous permet de savoir où
le robot peut passer ou non.

![Exemple de carte créée avec la classe `Bitmap`.](imgs/carte.png){#fig:carte width=100%}
