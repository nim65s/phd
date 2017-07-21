### Introduction Générale {#sec:intgen}

La robotique consiste à implémenter des facultés artificielles de perception, de décision et d’action dans une machine,
afin de lui permettre de réaliser une plus grande variété de tâches.

Grâce à un savant mélange d’électronique, d’informatique, de mécanique, de mathématiques, d’intelligence artificielle,
et d’automatique, la robotique a aujourd’hui bien dépassé le stade de science-fiction, où elle était encore confinée il
y a quelques décennies à peine.

En effet, la culture robotique est antérieure à ses applications industrielles et à la recherche qui y est associée. Le
terme robot lui-même trouve son origine en 1920 dans une pièce de théâtre tchécoslovaque de Karel Čapek. Il y désigne
un automate travailleur universel, dans le sens où il pourrait exécuter n’importe quelle tâche.

La création d’un tel automate universel n’aurait pas été possible avant les travaux d’Alan Turing sur la conception
d’ordinateurs pendant la seconde guerre mondiale. En effet, le premier automate industriel qui ait vocation à être
universel et puisse donc être qualifié de robot est un bras manipulateur d’assemblage pour les chaînes de production de
la General Motors nommé Unimate, et date des années 1960.

Entre temps, Isaac Asimov a eu le temps d’introduire les « Trois lois de la robotique » dans ses romans de
science-fiction dès les années 1940. Puis, dans les années 1950, les enfants japonais ont à leur tour pu découvrir la
robotique avec le manga « Astro, le petit robot » d’Osamu Tezuka.

Ce manga a initié un nouveau genre, celui des « Mecha », mettant en scène des armures robotisées humanoïdes.
De ce genre est par exemple issu l’univers de Gundam ([@fig:gundam]), une franchise créée dans les années 1980
comportant entre autres des films, des romans, des mangas, des animés et des jouets, et générant de nos jours
annuellement environ 50 milliards de yens, soit 500 millions d’euros.

Parmi les artistes qui ont travaillé pour cette franchise, on retrouve le designer Yutaka Izubuchi, qui a également
dessiné la première véritable plateforme de recherche en robotique humanoïde, HRP-2, financée par le programme japonais
« Humanoid Robotics Project ».

Suite à la création du JRL (CNRS/AIST), un laboratoire franco-japonais de robotique, le LAAS-CNRS est le seul
laboratoire à disposer d’une telle plateforme en dehors du Japon, et ce depuis 2006 : il s’agit d’HRP-2 14
([@fig:hrp2]).

<div id="fig:japon">
![HRP-2 14, au LAAS-CNRS, 2015.](imgs/hrp2.jpg){#fig:hrp2 height=12cm}
![Statue du Gundam RX-78-2 de taille réelle (18 mètres de haut), exposée de 2009 à 2017 sur l’île artificielle d’Odaiba
à Tokyo.](imgs/gundam.jpg){#fig:gundam height=12cm}

Robots humanoïdes japonais, dans la recherche à gauche, et dans la fiction à droite.
</div>

Les robots humanoïdes illustrent bien la robotique dans l’imaginaire. Cependant, dans la recherche et l’industrie, on
trouve des robots à roues dans bien plus d’applications et depuis bien plus longtemps que des robots humanoïdes.

Le robot mobile HILARE [@giralt79] ([@fig:hilare]) a par exemple été conçu à des fins de recherche au LAAS-CNRS, et a
eu trois version, en 1977, 1990 et 1999.

La recherche en robotique mobile a notamment abouti à la création de divers rovers lunaires et martiens
([@fig:curiosity]), utilisés par des scientifiques issus de tous domaines pour réaliser des expériences dans des
conditions inédites, et mieux comprendre notre système solaire.

Aujourd’hui, de nombreuses entreprises et laboratoires poursuivent encore la recherche en robotique mobile, entre
autres afin de robotiser nos voitures ([@fig:googlecar]), et de résoudre ainsi de nombreux problèmes engendrés par nos
moyens de transport actuels.

<div id="fig:mobilerecherche">
![HILARE au musée des Arts et Métiers en 2009.](imgs/hilare.jpg){#fig:hilare height=4.5cm}
![Autoportrait de Curiosity sur Mars en 2015.](imgs/curiosity.jpg){#fig:curiosity height=4.5cm}
![Google Car, une voiture robot.](imgs/googlecar.jpg){#fig:googlecar height=4.5cm}

Exemples de robots mobiles dans la recherche
</div>

L’industrie est également friande de robotique mobile, surtout grâce aux Automatic Guided Vehicle (AGV, [@fig:agv]) qui
permettent d’améliorer la gestion et les performances d’un entrepôt, et aux bras manipulateurs pouvant manier des
pièces et des outils sur les chaînes d’assemblage, mais aussi grâce à de plus modestes robots qui peuvent être vendus
en grandes séries directement au grand public, comme des aspirateurs ([@fig:roomba]) ou des tondeuses.

<div id="fig:mobileindustrie">
![Transpalette robotique conçu par l’entreprise BA Systèmes.](imgs/agv.png){#fig:agv height=6cm}
![Aspirateur robotique grand public Roomba.](imgs/roomba.jpg){#fig:roomba height=6cm}

Exemples de robots mobiles dans l’industrie.
</div>

<div id="fig:aldebaran">
![Nao, 58cm, 2005](imgs/nao.jpg){#fig:nao height=8cm}
![Pepper, 121cm, 2014](imgs/pepper.jpg){#fig:pepper height=8cm}

Robots d’Aldebaran Robotics prévus pour le grand public.
</div>

De nos jours, on trouve des applications à la robotique dans tous les domaines de l’industrie, que ce soit pour la
fabrication, la manutention, ou le contrôle qualité. On la retrouve également dans un nombre croissant d’autres
secteurs, comme la médecine, l’agriculture, les transports, ou encore le spatial.

De plus en plus, on retrouve également des robots dans notre quotidien, comme le Roomba ([@fig:roomba]) présenté
précédemment, ou encore Pepper ([@fig:pepper]), un robot français de forme humanoïde (mais qui se déplace grâce à trois
roues omnidirectionnelles), qui peut servir d’hôte d’accueil, et aussi son petit frère Nao ([@fig:nao]), utilisable
comme plate-forme didactique.

Enfin, la robotique mobile n’est pas non plus oubliée dans la science-fiction, comme le montrent les exemples de robots
mobiles bien connus donnés dans la [@fig:mobilefiction].

<div id="fig:mobilefiction">
![Dalek, *Dr Who*, 1963](imgs/dalek.jpg){#fig:dalek height=5cm}
![R2-D2, *Star Wars*, 1977](imgs/r2d2.jpg){#fig:r2d2 height=5cm}
![Wall-E, 2008](imgs/wall-e.jpg){#fig:walle height=5cm}

Exemples de robots mobiles dans la science-fiction.
</div>

En remplaçant ainsi l’homme dans un nombre croissant de tâches difficiles, répétitives, fastidieuses, voire
dangereuses, la robotique démontre à la fois son impact sur la société et son intérêt économique. Son impact sociétal
n’est cependant pas à prendre à la légère, comme nous allons le voir dans la [@sec:precautions].
