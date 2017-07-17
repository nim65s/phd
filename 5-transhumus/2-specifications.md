### Spécifications et solutions techniques {#sec:transspecs}

L’ambition poétique de ce projet est de libérer les arbres de leur immobilité et de les laisser explorer le monde par
eux-mêmes. Cette ambition impose la création de connections originales entre des éléments naturels et technologiques.

Cette inspiration continue le travail de Céleste Boursier-Mougenot de ces dernières années [@MacAdam].

La première étape de ce projet a été d’ouvrir un processus de dialogue avec l’artiste. Nous avons ainsi dû définir le
type d’arbres utilisés, leur occupation de l’espace dans les *Giardini*, ce que signifie pour un arbre de bouger
« de lui-même », et quelles sont les conditions de développement et d’exploitation.

#### Spécifications

Les spécifications qui suivent dans cette section sont issues de ce processus de dialogue avec l’artiste.

##### Arbres

Les arbres retenus pour ce projet sont des pins sylvestres, dont la floraison en mai coïncide avec l’ouverture de la
Biennale. Nous avons donc pris trois de ces arbres pour l’œuvre à Venise, plus un pour nos tests au LAAS-CNRS.

Ils font environ cinq mètres de haut. Ils sont vivants, et se déplacent avec leur motte de terre pour un total
d’environ trois tonnes.

##### Zones

Deux de ces arbres évoluent dans l’espace devant les pavillons français, anglais, canadien et allemand. Ils doivent
rester à l’intérieur d’une zone de 300 mètres carrés bien définie ([@fig:zones]). Le sol de cette zone est composée de
terre battue et de graviers, donc la dureté dépend des conditions météorologiques.

<div id="fig:zones">
![Vue aérienne des pavillons français (sur la gauche), anglais (en haut au centre), canadien (en haut à droite) et
allemand (sur la droite) autour d’une esplanade dans les *Giardini*](imgs/earth.jpg){width=100%}

![Modèle géométrique des zones d’évolution, avec une grille dont les carreaux font 10 mètres pour
l’échelle. Cette image est issue de l’interface utilisateur servant à monitorer le déplacement des
arbres.](imgs/plan_vierge.png){width=100%}

Vue aérienne de la partie des *Giardini* qui nous intéresse. Le pavillon français est le bâtiment sur la gauche. Un
arbre se déplace dans la salle principale de ce pavillon, et les deux autres se partagent l’esplanade commune aux
pavillons anglais, canadien et allemand.
</div>

Le troisième arbre se déplace lui dans le pavillon français, dans une zone de 50 mètres carrés pourvue d’un sol en
béton.

Ces deux zones ne comportent pas d’obstacles permanents, mais sont des aires de passage de visiteurs sans contraintes
spécifiques de sécurité. Ces visiteurs sont autorisés à approcher et toucher les arbres.

##### Origine du mouvement

Les arbres sont des êtres vivants, dont le métabolisme dépend des conditions environnementales et météorologiques. Leur
mouvement doit dépendre des variations de leur état interne. Ceci est l’une des principales problématiques de ce
projet: cette œuvre cherche à révéler l’invisible état interne des arbres.

Il est également nécessaire de restreindre le mouvement des arbres aux zones définies dans la section précédente, et
d’éviter les collisions entre les deux arbres qui partagent l’esplanade.

##### Qualité du mouvement

L’artiste tient à ce que les arbres bougent extrêmement lentement. Avec une vitesse inférieure au mètre par minute,
leurs mouvements doivent être à peine perceptibles. Les arbres doivent bouger sans avoir une direction privilégiée: ils
devraient être holonomes.

Aucun bruit ne doit être audible pour les visiteurs, les arbres doivent donner l’impression de se mouvoir par
lévitation. La base de la motte de terre doit être à moins de 5cm du sol.

##### Contraintes opérationnelles

Le projet doit être réalisé en six mois sans aucune extension possible de date limite, fixée à l’ouverture de la
biennale, le 5 mai 2015, avec seulement deux semaines de tests sur site.

L’œuvre doit fonctionner jusqu’au 22 novembre 2015, à raison de 8 heures par jour et 6 jours par semaine. Elle doit
être utilisable par l’équipe de non-spécialistes du pavillon français en une journée de formation.

#### Solutions technologiques

Ces spécifications ont conduit aux solutions technologiques suivantes.

##### Conception de la plate-forme

Des plate-formes robotiques sur mesure ont été conçues par BA Système, une société spécialisée dans la conception et la
production d’AGV (Automatic Guided Vehicles) pour la logistique.

Chaque plate-forme est composée d’un bac octogonal supporté par trois tourelles [@fig:pot], composées d’une roue
motrice électrique, orientable autour de son axe central. Les roues peuvent donc tourner sur place.

![AGV dans les locaux de BA Systèmes](imgs/capture_video_BA.jpg){#fig:pot height=5cm}

Le bruit des moteurs électriques de traction et d’orientation sont inaudibles.

Cela ne rend pas la plate-forme holonome, mais bien omnidirectionnelle, de type $(1, 2)$ dans la classification de
@campion96. On peut donc contrôler la plate-forme dans chacune des trois directions de $\mathbb{R}^2\times S^1$.
Le modèle de contrôle utilisé est présenté dans la [@sec:transmodel].

Les mottes des arbres sont insérées dans les bacs, et des coquilles synthétiques imitant la terre et les racines
encapsulent les AGVs. Les coques synthétiques contribuent également à la suppression totale de légers bruits qui
pourraient provenir des moteurs.

##### Capteur du métabolisme des arbres

La sonde Granier [@granier] ([@fig:needles]) est l’une des techniques les plus courantes pour mesurer le métabolisme
d’un arbre [@lu2004]. La sonde est fondée sur un principe de dissipation thermique, et est constituée de deux
aiguilles.

Une aiguille chauffée est placée dans l’aubier au-dessus d’une aiguille neutre. Quand la vitesse de la sève est faible,
la chaleur de l’aiguille chauffée est peu dissipée, et la différence de température entre les deux aiguilles est donc
élevée. Cette différence diminue avec l’augmentation de la vitesse de la sève.

Sur le pin sylvestre  installé au LAAS-CNRS, nous avons vérifié que la sensibilité de ces sondes était suffisante pour
observer une différence de luminosité ([@fig:mesures]).

<!--TODO figure check sondes-->

Cette luminosité change avec les conditions atmosphériques, ainsi que lorsque que l’arbre se déplace entre l’ombre et
la lumière. Nous installons alors dans chaque arbre trois sondes dans différentes directions. Les mesures données par
les sondes sont ensuite utilisées comme des entrées pour la génération de mouvement.

<div id="fig:granier">
![Capteurs de flux de sève: les sondes Granier sont composées de deux aiguilles
thermocouples](imgs/sapflow.jpg){#fig:needles}
![Déplacement d’un arbre de l’ombre à la lumière et vice-versa: mesures d’une sonde Granier sur l’arbre de test au
LAAS-CNRS les 8 et 9 avril 2015, entre 12:00 et 18:00, lorsque l’on déplace l’arbre aux alentours de
15:00.](imgs/granier.png){#fig:mesures width=6cm}

Mesures du flux de sève: ces expériences nous ont permis de vérifier cette solution technique par rapport à nos
spécifications. Nous avons constaté que la réaction d’un arbre passant de l’ombre à la lumière était mesurable et
donc exploitable en tant qu’entrée de notre système, puisque le métabolisme des arbres peut influer sur leur
déplacement.
</div>

##### Localisation {#sec:transloc}

Les aires d’évolution sont définies à l’intérieur et à l’extérieur du pavillon français. Pour localiser les AGV, nous
avons donc opté pour une technologie UWB (Ultra Wide Band) développée par la société Ubisense. Cette technologie nous
apporte un bon compromis entre la précision et la discrétion.

Les bâtiments autour des zones d’évolution des arbres sont équipés d’antennes assurant une couverture complète
([@fig:ubisense]). Les arbres sont équipés de plusieurs petits récepteurs cachés dans les branches.

Une antenne ayant un rôle de maître interroge régulièrement les récepteurs un à un. Lorsque celui-ci répond, chaque
antenne mesure l’angle d’arrivée du signal ainsi que la durée de la transmission.

Les données de triangulation, de trilatération et les informations connues sur la position relatives de plusieurs
récepteurs installés dans un même arbre (considéré rigide) sont ensuites filtrées.

Une précision de l’ordre de 15 centimètres est obtenue avec un bon niveau de qualité.

![Implantation des antennes UWB Ubisense dans les *Giardini*](imgs/plan_capteurs.png){#fig:ubisense width=90%}
