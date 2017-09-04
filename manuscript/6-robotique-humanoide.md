# Étude de la robotique humanoïde {#sec:humanoide}

\input{manuscript/partstart}

## Introduction: La locomotion bipède {-}

Après avoir exploré la robotique mobile avec les robots à roues, nous passerons dans cette partie à un autre mode de
déplacement en examinant les bipèdes.

L’étude de la marche bipède a trois intérêts majeurs:

- Mieux comprendre la locomotion humaine [@arechavaleta08],
- Créer des prothèses pour aider des personnes à se déplacer [@mombaur17].
- Créer des robots capables de se déplacer et d’agir dans un environnement façonné par et pour l’homme,

Ces dernières années, la conception et la fabrication de robots bipèdes a largement évolué. On trouve désormais
régulièrement des vidéos, réalisées à destination du grand public, où l’on pourrait croire que des robots bipèdes sont
prêts à être utilisés de façon commerciale. C’est notamment le cas avec les vidéos de sociétés comme Boston Dynamics
([@fig:atlas]) ou Agility Robotics ([@fig:cassie]), où l’on voit des robots bipèdes, de taille humaine, qui semblent
suffisamment à l’aise pour se déplacer seuls sur des types de sols allant du béton plat à une pente en forêt recouverte
de neige, ou même pour sauter des escaliers.

<div id="fig:videos">
![Atlas, Boston Dynamics](imgs/atlas.jpg){#fig:atlas width=49%}
![Cassie, Agility Robotics](imgs/cassie.jpg){#fig:cassie width=49%}

Captures d’écrans de vidéos de Boston Dynamics et Agility Robotics.
Ces robots bipèdes semblent être livrés à eux-mêmes en pleine nature.
</div>

Cependant, comme l’a remarqué @moravec88, le mouvement est un problème complexe. Plus récement, le DARPA Robotics
Challenge nous a montré ce que l’état de l’art permettait de réellement accomplir dans un contexte de tests réalistes
[@atkeson16]. Sans surprise, même les meilleures équipes du monde sont encore loin de pouvoir créer un robot
accomplissant une série de tâches pourtant triviales pour un enfant.

La locomotion bipède n’est pas un problème simple. L’être humain a besoin d’une à trois années pour la contrôler, alors
que d’autres moyens de locomotion sont maîtrisés dès la naissance chez les animaux.

Pour étudier la marche, de nombreuses machines ont été créées.

<div id="fig:bipedesactifs">
![Ruina, 2001](imgs/ruina.jpg){#fig:ruina height=9.5cm}
![Ikemata, 2006](imgs/ikemata.jpg){#fig:ikemata height=9.5cm}

Robots bipèdes passifs.
</div>

Certaines sont purement mécaniques ([@fig:bipedesactifs]), et étaient initialement des jouets bipèdes qui
descendaient passivement une pente.
<!--Pour décrire leur fonctionnement, on utilise une analogie avec une roue de vélo qui n’aurait pas de pneu.-->
Elles ont commencé à être étudiées par @mcgeer90 dans les années 1990, puis ont conduit à des travaux de complexité
croissante, notamment à Delft [@wisse07].

À l’opposé, d’autres machines ont dès le début été dotées d’un nombre important de capteurs et d’actionneurs puissants,
et constituent donc de véritables robots ([@fig:bipedespassifs]). Celles-ci ont été d’abord étudiées et développées au
Japon [@sakagami02, @kaneko02] dans les années 2000.

<div id="fig:bipedespassifs">
![Asimo, Honda, 2000](imgs/asimo.jpg){#fig:asimo height=8cm}
![Valkyrie, NASA, 2013](imgs/valkyrie.jpg){#fig:valkyrie height=8cm}
![Talos, PAL Robotics, 2017](imgs/pyrene.jpg){#fig:pyrene height=8cm}
<!--TODO: Photo de pyrène au LAAS-CNRS par xxx-->

Robots bipèdes actifs.
</div>

<!--[^11]: Ces dernières années, de nombreux laboratoires et industriels américains se sont emparés du sujet et ont bien fait-->
<!--avancer la recherche dans ce domaine ([@fig:videos]), mais le géant japonais Softbank vient de racheter deux des-->
<!--principales entreprises du secteur (Boston Dynamics et Schaft) aux américains, alors que les financements fédéraux de-->
<!--la recherche ont subi de lourdes coupes sous l’adminstration Trump.-->

Dans un premier temps, ces machines actives ont utilisé des mouvements quasi-statiques. Autrement dit, à tout instant,
la projection de leur centre de masse sur le sol restait dans le polygone support. Or, si une locomotion constituée
d’une série de poses à l’équilibre statique est simple et a donc de bonnes chances de fonctionner, elle présente
certains inconvénients. Parmi ces inconvénients, on citera notamment une faible vitesse, une grande consommation
énergétique, et une démarche peu pertinente. Ainsi, pour @grizzle10, en locomotion, le régime permanent correspond à
des solutions périodiques et non des équilibres statiques.

En utilisant des moteurs plus puissants et des contrôleurs plus complexes, on est aujourd’hui en mesure de générer des
mouvements de locomotion dynamique bien plus convaincants, mais qui restent loin de ce que l’on retrouve chez les
êtres vivants.

Dans le chapitre [-@sec:yoyoman], nous verrons une méthode ayant pour objectif de concevoir de manière optimale des
robots tirant parti de leur inertie comme un marcheur passif, tout en étant actionné par des moteurs, et donc
contrôlables.

\input{manuscript/partend}
