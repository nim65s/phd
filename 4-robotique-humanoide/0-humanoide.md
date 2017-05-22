# Étude de la robotique humanoïde

## Introduction: Les robots bipèdes {-}

Après avoir exploré la robotique mobile avec les robots à roues, nous passerons dans cette partie à un autre mode de
déplacement en examinant les bipèdes.

L’étude de la marche bipède a trois intérêts majeurs:

- Mieux comprendre la locomotion humaine,
- Créer des robots capables de se déplacer et d’agir dans un environnement façonné par et pour l’homme,
- Créer des prothèses pour aider des personnes à se déplacer.

Ces dernières années, la conception et la fabrication de robots bipèdes a largement évolué. On trouve désormais
régulièrement des vidéos, réalisées à destination du grand public, où l’on pourrait croire que des robots bipèdes sont
prêts à être utilisés de façon commerciale. C’est notamment le cas avec les vidéos de sociétés comme Boston Dynamics ou
Agility Robotics, où l’on voit des robots bipèdes, de taille humaine, qui semblent suffisamment à l’aise pour se
déplacer seuls sur des types de sols allant du béton plat à une pente en forêt recouverte de neige, ou même pour sauter
des escaliers.

Cependant, le DARPA Robotics Challenge nous a montré ce que l’état de l’art permettait de réellement accomplir dans un
contexte de tests réalistes [@atkeson16]. Sans surprise, même les meilleures équipes du monde sont encore loin de
pouvoir faire un robot accomplissant une série de tâches pourtant triviales pour un être humain.

La locomotion bipède n’est pas un problème simple. L’être humain a besoin d’une à trois années pour la contrôler, alors
que d’autres moyens de locomotion sont maîtrisés dès la naissance chez les animaux.

### Des machines pour étudier la locomotion bipède {-}

Pour étudier la marche, de nombreuses machines ont été créées.

Certaines sont purement mécaniques, et étaient initialement des jouets bipèdes qui descendaient passivement une pente.
<!--Pour décrire leur fonctionnement, on utilise une analogie avec une roue de vélo qui n’aurait pas de pneu.-->
Elles ont commencé à être étudiées par [@mcgeer90] dans les années 1990, puis ont conduit à des travaux de complexité
croissante, notamment à Delft [@wisse07].

À l’opposé, d’autres machines ont été dès le début dotées d’un nombre important de moteurs, et constituent donc de
véritables robots. Celles-ci ont été d’abord étudiées et développées au Japon [@sakagami02, @kaneko02] dans les années
2000. Elles ont en premier lieu été utilisées pour produire des mouvements quasi statiques. Or, si une locomotion
constituée d’une série de poses à l’équilibre statique est simple et a donc de bonnes chances de fonctionner, elle
présente certains inconvénients: faible vitesse et grande consommation énergétique.

En utilisant des moteurs plus puissants et des contrôleurs plus complexes, on est aujourd’hui en mesure de générer des
mouvements de locomotion dynamique bien plus convainquants, mais qui restent loin de ce que l’on retrouve chez les
êtres vivants.

Dans le chapitre \ref{cyoyoman}, nous verrons une méthode ayant pour objectif de concevoir des robots tirant parti de
leur inertie comme un marcheur passif, tout en étant actionné par plusieurs moteurs.
