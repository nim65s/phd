### Résultats {#sec:transresults}

Dans cette section, nous exposons les résultats opérationnels de ce projet, qui s’est terminé le 22 novembre 2015.

#### Interface utilisateur

L’interface utilisateur est composée d’une carte du pavillon et de l’esplanade des *Giardini*. les AGVs sont présentés
dans leur position et orientation actuelle, d’après le système de géolocalisation vu dans la [@sec:transloc], comme on
peut le voir dans la [@fig:wui].

![Capture d’écran de l’interface utilisateur, dans sa version avancée, en production le 9 septembre 2015. On peut y
voir les AGVs ainsi que leurs traces de 10:30 (heure à laquelle l’interface a été lancée) à 10:45. Il y a également une
table indiquant le status de chaque AGV ainsi que certains contrôles.](imgs/real_sim.png){#fig:wui width=100%}

Un panneau de contrôle est également disponible sous cette carte, donnant divers indicateurs numériques ainsi qu’une
série de contrôles simplifiant les opérations de maintenance que l’équipe du pavillon pourrait avoir à faire. Ceci
évite la plupart du temps le besoin de brancher un joystick directement sur l’AGV pendant l’exploitation, notamment
lors de la présence d’un obstacle inattendu, ou de problèmes dans la stabilité du sol à certains endroits.

#### Simulateur

La courte période de test sur place combinée à l’extrême lenteur attendue des AGV nous a imposé de régler le système à
l’aide d’un simulateur.

Cela a permis de rapidement vérifier la manière dont réagirait le système de génération de trajectoire dans différentes
situations, alors que cela aurait prit des semaines à vérifier en temps réel.

Les blocks logiciels de ce simulateur sont les mêmes que ceux décrits dans la [@fig:soft], à l’exception des blocks AGV
et géolocalisation qui sont remplacés par un seul module de simulation. Les données des sondes Granier utilisées en
simulation provenaient de plusieurs jours d’enregistrements sur l’arbre de test au LAAS-CNRS.

Sur la [@fig:simus], nous montrons un exemple des trajectoires qui peuvent être exécutés par les arbres, ainsi que les
marques qui seraient laissées au sol par les roues dans pour de telles trajectoires.

<div id="fig:simus">
![Trajectoire du centre des AGVs](imgs/simulateur-tracks-right-centre.png){width=100%}

![Trajectoire des roues des AGVs](imgs/simulateur-tracks-right.png){width=100%}

Exemple de simulation avec en haut les trajectoires des centres des AGV et en bas les trajectoires des roues des
AGVs. En temps réel, cela correspondrait à peu près à un voyage de 45 minutes. On remarque que les roues peuvent
parfois sortir des bordures, mais pas le tronc.
</div>

![Exemple de couverture d’espace en simulation. Sur site, un tel test aurait demandé plusieurs jours entre la fin de
l’installation matérielle et l’ouverture de la Biennale, ce que nous n’avions
pas.](imgs/covering.png){#fig:ressimulation width=100%}

#### Résultats expérimentaux

Pendant les premiers jours de l’installation matérielle, nous avons remarqué que les roues des AGVs peuvent être très
rapidement réorientée. Cette rapidité de réponse est bénéfique aux premiers tests de fonctionnement, mais pose tout de
même certains problèmes par la suite:

- Une réorientation rapide rend les moteurs audibles;
- Un ample mouvement angulaire du pneu et trop rapide par rapport à la traction laisse une marque permanente sur le sol
  en béton à l’intérieur du pavillon français;
- Un tel mouvement produit également un désagréable mouvement de crissement;
- En fonction de l’humidité du sol de l’esplanade, un changement brusque dans l’orientation d’une tourelle risque de
  creuser une petite tranchée. Ensuite, si une tranchée est trop profonde ou si les trois roues se retrouvent dans des
  tranchées, l’AGV court un fort risque d’embourbement.

Dans ces circonstances, notre réaction a été d’implémenter des composants de lissage des trajectoires, vus en
[@sec:translissage].

Par ailleurs, la configuration logicielle des paramètres de géolocalisation n’était pas parfaite du premier coup, comme
on peut le voir sur la [@fig:carres]. Dans la majorité des situations, le système de géolocalisation fonctionnait bien
mais dans certains cas nous avions des perturbations entraînant des comportements inadmissibles pour les AGVs.

<div id="fig:carres">
![Réussite](imgs/carre_ok.png){width=30%}
![Échec](imgs/carre_ko.png){width=45%}

Essais de suivi de figures simples par un AGV, pendant la phase d’installation matérielle de la biennale. La figure de
gauche correspond à une réussite totale sur plusieurs tours, tandis que sur la figure de droite, on comprend que le
système de géolocalisation est perdu.
</div>

Ces problèmes ont été résolus en réglant au mieux les paramètres des algorithmes d’Ubisense, ce qui n’aurait pas été
possible sans l’aide d’ingénieurs de cette entreprise.

Vu la vitesse des robots (un mètre par minute au maximum), la sécurité n’a jamais été pas un problème majeur. L’équipe
du pavillon avait accès à l’interface web grâce à une tablette qu’ils pouvaient garder avec eux, et ils avaient
également une télécommande d’arrêt d’urgence qui coupait directement la puissance dans le pire des cas.

Au fur et à mesure de l’exposition, le mode nominal de fonctionnement de cette œuvre a été de plus en plus utilisé, de
quelques heures par jour lors de l’ouverture, jusqu’à des semaines entières lors de l’été, lorsque les problèmes liés à
la configuration du système de géolocalisation ont été définitivement réglés.

Le principal problème restant lors de l’exploitation de cette installation a été la pluie. Venise est connue pour ses
fortes pluies, qui pouvaient régulièrement rendre la zone extérieure totalement impraticable pour les robots.
Heureusement, cela n’empêchait pas le public de voir l’œuvre fonctionner dans le pavillon, même si la verrière de la
salle principale avait été retirée pour laisser l’arbre respirer. Les salles périphériques pouvaient alors offrir un
refuge aux visiteurs.

Les spécifications sur le bruit ont été respectées, si bien que le public ne se rendait pas forcément compte que les
arbres bougaient. Et une fois qu’une personne le remarquait, elle se demandait comment des arbres pouvaient bouger.
