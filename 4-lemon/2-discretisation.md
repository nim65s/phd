### Création de la carte {#sec:carto}

Dans cette section, nous partons d’un plan généré par les capteurs laser du robot, constitué d’une liste d’obstacles.

Afin de réaliser des tests de performances dans un maximum de cas, ce plan peut provenir de différentes sources :

- un fichier texte généré par le prototype de BA Système composé de deux nombres par lignes indiquant les coordonnées de
  chaque point obstacle trouvé par les lasers,
- une image au format PNG ou BMP (par exemple un plan d’architecte) et d’une échelle,
- en utilisant directement l’API de la librairie implémentée pour l’occasion.

L’objectif est d’extraire la position des murs de ce nuage de point, afin de générer des trajectoires de balayage des
bords de ces murs. On a aussi besoin de pouvoir savoir où le robot peut passer ou non.
