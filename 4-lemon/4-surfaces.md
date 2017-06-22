### Trajectoires de nettoyage des surfaces {#sec:surfaces}

Dans cette section, nous présentons la stratégie de balayage des surfaces retenue. Ce balayage de surface intervient
après le balayage des bordures.

De la première transformée de Hough pour la détections des segments de droites (*cf.* [@sec:borduresdroites]), nous
extrayons la droite de la transformée de Hough ayant le plus de `Pixels`.

Depuis cette droite principale, nous traçons des segments parrallèles qui couvrent la surface, tout en prenant toujours
soin d’éviter les collisions avec l’environnement grâce à la procédure \textsc{followLine} décrite dans
l’alg. \ref{alg:segments}.

De chaque segment ainsi généré, nous ajoutons deux trajectoires dites « symmétriques » à la `Roadmap`, qui
correspondent aux deux sens de parcours du segment par la brosse principale du robot.

Il suffit alors qu’une des deux trajectoires de la paire soit suivie par le robot pour considérer que la paire est
traitée.
