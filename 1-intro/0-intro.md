## Introduction Générale {-}

La robotique consiste à augmenter l’autonomie d’une machine, en lui donnant des facultés de perception, de décision et
d’action.

Grâce à un savant mélange d’électronique, d’informatique, de mécanique, de mathématiques, d’intelligence artificielle,
et d’automatique, elle a aujourd’hui bien dépassé le stade de science-fiction, où elle était encore confinée il y a
quelques décennies à peine.

En effet, la culture robotique est antérieure à ses applications industrielles et à la recherche qui y est associée. Le
terme robot lui-même trouve son origine en 1920 dans une pièce de théâtre tchécoslovaque de Karel Čapek. Il y désigne
un automate travailleur universel, dans le sens où il pourrait exécuter n’importe quelle tâche.

Le premier automate industriel qui ait vocation a être universel, Unimate, est un bras manipulateur d’assemblage pour
les chaînes de production de la General Motors, et date des années 1960.

Entre temps, Isaac Asimov a eu le temps d’introduire les « Trois lois de la robotique » dans ses romans de
science-fiction dès les années 1940. Puis, dans les années 1950, les enfants japonais ont à leur tour pu découvrir la
robotique avec le manga « Astro, le petit robot » d’Osamu Tezuka.

Ce manga a initié un nouveau genre, celui des « Mecha », mettant en scène des armures robotisées humanoïdes.
De ce genre est par exemple issu l’univers de Gundam ([@fig:gundam]), une franchise créée dans les années 1980
comportant entre autres des films, des romans, des mangas, des animés et des jouets, et générant de nos jours
annuellement environ 50 milliards de yens, soit 500 millions d’euros.

Parmis les artistes qui ont travaillé pour cette franchise, on retrouve le designer Yutaka Izubuchi, qui a également
dessiné la première véritable plateforme de recherche en robotique humanoïde, HRP-2, financée par le programme japonais
« Humanoid Robotics Project ».

Suite à la création du JRL (CNRS/AIST), un laboratoire franco-japonais de robotique, le LAAS-CNRS est le seul
laboratoire à disposer d’une telle plateforme en dehors du Japon, et ce depuis 2006 : il s’agit d’HRP-2 14
([@fig:hrp2]).

\newpage

<!--TODO spécifier la hauteur des images-->

<div id="fig:japon">
![HRP-2 14, au LAAS-CNRS en 2015](imgs/hrp2.jpg){#fig:hrp2 width=44%}
![Statue du Gundam RX-78-2 de taille réelle (18 mètres de haut), exposée de 2009 à 2017 sur l’île artificielle d’Odaiba
à Tokyo](imgs/gundam.jpg){#fig:gundam width=56%}

Robots humanoïdes japonais, dans la recherche à gauche, et dans la fiction à droite.
</div>

Les robots humanoïdes illustrent bien la robotique dans l’imaginaire, mais en pratique on trouve des robots à roues
dans bien plus d’applications et depuis bien plus longtemps.

Le robot mobile HILARE [@giralt79] ([@fig:hilare]) a par exemple été conçu à des fins de recherche au LAAS-CNRS, et a
eu trois version, en 1977, 1990 et 1999.

La recherche en robotique mobile a notamment abouti à la création de divers rovers lunaires et martiens
([@fig:curiosity]), utilisés par les scientifiques issus de tous domaines pour réaliser des expériences dans des
conditions inédites, et mieux comprendre notre système solaire.

Ajourd’hui, de nombreuses entreprises et laboratoire font encore de la recherche en robotique mobile afin de robotiser
nos voitures ([@fig:googlecar]), et de résoudre ainsi de nombreux problèmes engendrés par nos moyens de transport
classiques.

<div id="fig:mobilerecherche">
![HILARE au musée des Arts et Métiers en 2009](imgs/hilare.jpg){#fig:hilare width=40%}
![Autoportrait de Curiosity sur Mars en 2015](imgs/curiosity.jpg){#fig:curiosity width=23%}
![Google Car, une voiture robot](imgs/googlecar.jpg){#fig:googlecar width=35%}

Exemples de robots mobiles dans la recherche
</div>

L’industrie est également friande de robotique mobile, surtout grâce aux Automatic Guided Vehicle (AGV, [@fig:agv]) qui
permettent d’améliorer la gestion et les performances d’un entrepôt, mais aussi grâce à de plus modestes robots qui
peuvent être vendus directement au grand public, comme des aspirateurs ([@fig:roomba]) ou des tondeuses.

<div id="fig:mobileindustrie">
![Transpalette robotique conçu par l’entreprise BA Systèmes](imgs/agv.png){#fig:agv width=39%}
![Aspirateur robotique grand public Roomba](imgs/roomba.jpg){#fig:roomba width=50%}

Exemples de robots mobiles dans l’industrie
</div>

Enfin, la robotique mobile n’est pas non plus oubliée dans la science-fiction, comme le montrent les exemples de robots
mobiles bien connus donnés dans la [@fig:mobilefiction].

<div id="fig:mobilefiction">
![Dalek, *Dr Who*, 1963](imgs/dalek.jpg){#fig:dalek width=39%}
![R2-D2, *Star Wars*, 1977](imgs/r2d2.jpg){#fig:r2d2 width=30%}
![Wall-E, 2008](imgs/wall-e.jpg){#fig:walle width=39%}

Exemples de robots mobiles dans la science-fiction
</div>

De nos jours, on trouve des applications à la robotique dans tous les domaines de l’industrie, que ce soit pour la
fabrication, la manutention, ou le contrôle qualité. On la retrouve également dans un nombre croissant d’autres
secteurs, comme la médecine, l’agriculture, les transports, ou encore le spatial.

En remplaçant ainsi l’homme dans un nombre croissant de tâches difficiles, répétitives, fastidieuses, voire
dangereuses, elle démontre son impact sur la société ainsi que son intérêt économique.

De plus en plus, on retrouve également des robots dans notre quotidien, comme le Roomba ([@fig:roomba]) présenté
précédemment, ou encore Pepper, un robot français de forme humanoïde (mais qui se déplace grâce à trois roues
omnidirectionnelles), qui peut servir d’hôte d’accueil, et son petit frère Nao, utilisable comme plate-forme didactique.

<div id="fig:aldebaran">
![Nao, 2005, 58cm](imgs/nao.jpg){#fig:nao width=22%}
![Pepper, 2014, 121cm](imgs/pepper.jpg){#fig:pepper width=17%}

Robots d’Aldebaran Robotics prévus pour le grand public
</div>
