### Architecture Matérielle et Logicielle

Dans un premier temps, l’artiste voulait que les pianos soient « maîtres d’eux-mêmes », et donc que nous embarquions
tous nos algorithmes dans de petits ordinateurs à leur bord.

Sur le plan théorique, cela ne change pas grand-chose. Les batteries de voitures déjà embarquées sur les pianos
suffisent largement à alimenter en plus un mini ordinateur de type Raspberry Pi ou NUC/Brix suivant la puissance de
calcul requise.

Cependant, en termes de complexité de déploiement, le coût en temps était trop élevé. De plus, les choix présentés en
[@sec:perception] imposaient la présence d’une interface utilisateur dans le musée.

Nous avons donc utilisé une architecture centralisée, où un ordinateur de bureau, muni d’un écran, d’un clavier et
d’une souris, restait à disposition de l’équipe du musée, et servait à orchestrer les déplacements des
pianos.

La [@fig:overview] explique l’architecture matérielle utilisée pour cette œuvre.

![Architecture matérielle de l’œuvre *off road*.](imgs/overview.png){#fig:overview width=100%}

On y retrouve deux caméras décrites à la [@sec:perception], attachées au plafond, reliées par USB directement sur
l’ordinateur principal.

Un module XBEE est également connecté à cet ordinateur, et envoie des ordres aux pianos grâce au protocole ZigBee.

Sur les pianos, on retrouve ces différents composants:

* Une batterie de voiture 12V 120Ah
* Deux moteurs
* Un module XBEE pour recevoir les ordres de l’ordinateur principal ([@fig:xbee])
* Un accéléromètre pour détecter les chocs
* Un capteur de courant par sécurité
* Une carte de contrôle moteur 60A ([@fig:sabertooth])
* Un Arduino ([@fig:arduino]) qui implémente l’[@eq:differentiel], gère les autres composants électroniques, et remonte
  des données sur l’état courant à l’ordinateur principal
* Un « shield » Arduino sur mesure pour connecter tous ces composants électroniques ([@fig:shield])

Enfin, la station météo ([@fig:meteo]) est connectée à un Arduino qui interprète les données analogiques, et les envoie
à une Raspberry Pi ([@fig:raspi]) en USB, qui à son tour les transmet à l’ordinateur principal en ethernet grâce à la
librairie ZeroMQ.

Cette solution a été choisie puisque d’une part nous avions déjà tous les composants nécessaires, et d’autre part il y
a besoin de plusieurs dizaines de mètres de câbles. L’ethernet est donc l’une des seules liaisons physiques viables.

Tous ces composants sont illustrés sur la [@fig:offroadcomponents].

<div id="fig:offroadcomponents">
![Raspberry Pi, un ordinateur avec un processeur ARM de la taille d’une carte de crédit.](imgs/raspi.jpg){#fig:raspi
width=55%}
![Arduino, un microcontrolleur simple d’utilisation.](imgs/arduino.jpg){#fig:arduino width=35%}

![Module XBEE, pour transmettre des données sans fil.](imgs/xbee.jpg){#fig:xbee width=45%}
![Carte de contrôle moteurs.](imgs/sabertooth.png){#fig:sabertooth width=45%}

![Layout du shield Arduino conçu sur mesure. L’effet miroir est inhérent à la technologie utilisée pour graver le
circuit imprimé.](imgs/kennim.png){#fig:shield height=5cm}
![Schéma électrique de la girouette et de l’anémomètre utilisé.](imgs/analog.png){#fig:meteo height=5cm}

Composants matériels utilisés pour *off road*.
</div>

Une manette de XBOX était également fournie et branchée sur l’ordinateur principal, afin de pouvoir déplacer
manuellement les pianos.

Du point de vue logiciel, tous nos développements ont été effectués en C pour les microcontrolleurs et en Python pour
le reste.

Le protocole de communication entre les arduinos des pianos et l’ordinateur principal a été créé sur mesure.
