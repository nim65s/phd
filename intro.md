À faire:

- mail de soutenance / résumé
- slides classes de robots: schémas ?
- titre de la section bipède / nom du projet: actanthrope ? yoyoman ?

# Introduction Générale

## slide titre

La robotique consiste à implémenter des facultés artificielles de perception, de décision et d’action
dans une machine, afin de lui permettre de réaliser une grande variété de tâches.

Pour cela, la robotique est intimement liée à la notion de mouvement. Ce mouvement caractérise généralement
le monde vivant, et plus particulièrement le règne animal; mais si l’on dote une machine de facultés de manipulation
d’objects et de locomotion, elle devient capable de seconder voire remplacer l’être humain, notamment pour des travaux
qui seraient difficiles, répétitifs, fastidieux, voire dangereux.

## slide intro

Cette thèse se concentre sur la génération de mouvements de locomotion terrestre.
Parmi les modes de locomotion terrestre, on retrouve principalement le roulement sans glissement chez les robots à
roues ainsi que la marche chez les robots bipèdes.
Ces deux modes de locomotion constitueront les deux principales parties de cet exposé.

# Introduction Partie mobile

## slide robotique mobile

Commençons par les robots mobiles.

Ces robots à roues sont étudiés dans le monde académique depuis plusieurs décénies, et la théorie concernant leur
modélisation et leur contrôle est largement mature. On peut d’ailleurs observer l’arrivée de ces robots mobiles sur le
marché grand public, notamment par le biais de petits aspirateurs autonomes, mais également, et de plus en plus, sur le
marché automobiles. En effet, ce secteur est depuis peu poussé vers la robotisation par l’arrivée de nouveaux acteurs
tels que l’entreprise Tesla.

Les contributions de cette thèse dans ce domaine de la robotique mobile sont essentiellement applicatives plutôt
que théoriques.

Dans cette première partie, nous ferrons le rapport de la réalisation de trois projets dont le but a été de générer des
mouvements pour des robots à roues.

Dans les trois cas, nous retrouverons une démarche similaire, débutant par une réflexion sur les qualités
recherchées d’un mouvement dans un contexte particulier, et se terminant par une mise en œuvre concrète sur des robots.

Chacun de ces projets utilise des robots de classes différentes, commeçons donc par une présentation des cinq
différentes classes de robots mobile existantes.

<!--intro art et robotique: transcrire-->

## slide 5 classes de robots mobiles

Cette analyse se fonde sur l’étude des différents type de roues existant ainsi que de la manière d’utiliser ces roues
sur un robot donné. À partir de là, on introduit les notions de degré de mobilité et dirigeabilité d’un robot.

Le premier correspond au nombre de degrés de libertés pouvant être directement contrôlés, et
le second correspond au nombre de roues pouvant être indépendamment réorientées afin de diriger le robot.
Ces deux nombre définissent la classe d’un robot.

Prenons la classe (2, 0), représentant donc les robots mobiles à deux degrés de mobilité et 0 degrés de dirigeabilité.
Ces robots, que l’on appelle communément des robots différentiels, sont les plus simple à contrôler. Ils sont
principalement constitués de deux roues motrices co-axiales, et la différence de vitesse de ses roues influe
directement sur la trajectoire qui sera suivie par le robot.

Si l’on considère ensuite la classe (1, 1), nous avons des robots pouvant se comporter comme des voitures. La
principale différence avec les robots précédents est que leur rayon de braquage est limité. Cette borne dépend
notamment de la distance entre les roues fixes et les roues orientables d’un tel robot.

[…]

# Introduction Offroad

## Slide offroad

Dans cet exemple introductif, nous allons voir la réalisation d’une œuvre d’art ayant essentiellement consisté à générer
des trajectoires pour des robots différentiels. Le principal défi de ce projet a été de retranscrire en termes
technologiques les descriptions poétiques de l’artiste sur les qualités finales des mouvements qu’il désirait.

Commençons par resituer le contexte de la création cette œuvre.

# Conclusion Offroad

## slide video offroad

Ce projet a été livré à temps pour le vernissage de l’exposition au Musée des abattoirs, et a fonctionné cinq jours
sur sept pendant 4 mois. Durant cette période, les seuls problèmes que nous avons rencontré ont été causés par notre
méthode de géolocalisation, dont les résultats pouvaient fortement varier avec l’éclairage ambiant, par exemple
lorsqu’une ampoule grillait. Un piano qui s’était perdu a notamment percuté un escalier, détruisant ainsi son pied
arrière avant que l’équipe du musée ne puisse l’arrêter. Ce piano a rapidement été écarté et réparé, et aucun autre
problème majeur ne s’est posé pendant l’exposition.

# Introduction transhumus

## slide transhumus

À la suite du projet Offroad, Céleste Boursier-Mougenot est revenu vers nous afin d’aller plus loin dans l’étude de
mouvements artistiques, et pour un projet bien plus ambitieux, qu’il a dénommé transhumus.

Nous avons qu’un arbre ne se déplace pas. L’ambition de ce projet a été précisément d’essayer le contraire.

# Conclusion transhumus

## slide video transhumus

Ce projet a été livré à temps pour l’ouverture de la 56ième Biennale de Venise, et a fonctionné six jours sur sept
pendant sept mois. Durant cette période, les principaux problèmes que nous avons rencontrés ont été la stabilité du sol
de l’esplanade, notamment en cas de fortes pluies. Nous avons aussi eu des problèmes de géolocalisation, causés par une
mauvaise configuration des filtres fournis par Ubisense, ce qui a rapidement été résolu par un ingénieur de leur
support technique.

Un second problème que nous avons rencontré concerne le choix initial de la classe du robot. Comme nous l’avons vu,
notre méthode de contrôle garanti l’unicité du CIR, et les échelles de temps couplées à un lissage rendent les
réorientations des tourelles très lisses. Cependant, il peut arriver que ce CIR se place au niveau d’une tourelle, et
on tombe alors dans un point singulier.

Cette œuvre sera à nouveau exposée sous peu au MONA de Tasamanie. Nous avons déjà formé le personnel de ce musée, et
modifié certains détails pour adapter la génération de mouvement aux contraintes de ce nouveau lieu.

# Intro Lemon

problème prosaique, qui est un problème classique, qui s’apparente aux robots aspirateurs, à la différence que là on
veut des mouvement beaucoup plus structurés.

# Conclusion lemon

## Démo lemon

L’implémentation de notre méthode dans un simulateur donne des résultats tout à fait satisfaisants, mais les
démonstrations réelles sur le robot n’ont pas été aussi bonnes pour deux raisons principales.

La première de ces raisons est le format initialement choisi pour que nous indiquions à BA les mouvements à
éxécuter par le robot. En effet, nous avions convenu de leur fournir une trajectoire discrétisée, et cette
discrétisation s’effectue au prix d’une perte d’information, et on perd par exemple systématiquement la localisation
théorique exacte de chaque point de rebroussement. Il est devient donc très difficile pour l’asservissement du robot de
suivre cette trajectoire fournie.

La seconde de ces raisons concerne le choix initial de la classe du robot. Pour qu’un robot de classe (1, 1)
puisse suivre une trajectoire comprenant un point de rebroussement, il est nécessaire que le robot s’arrête au niveau
de ce point pendant la durée nécessaire à la réorientation de sa roue, exactement comme lorsque que vous faites un
créneau avec votre voiture. Combiné avec le problème précédent, cela rend l’asservissement pratiquement impossible.

Ces deux problèmes sont liés, et sont de plus relativement simple à résoudre, à condition de reprendre la conception de
ce projet


# Conclusion Partie Mobile

## Slide ?

Dans cette partie, nous avons vu que même si la théorie concernant la modélisation et le contrôle de robots mobiles est
bien mature, la mise en œuvre en conditions réelles demande du travail.

les choix fait en amont qui semblent insignifiants sur la classe de robots conditionnent la suite
La qualité du mouvement dépend grandement des choix du design.

les modèles de robots introduisent des contraintes sur les mouvements, notamment dans l’espace de travail et pas le
dans l’espace des configurations

# Introduction Partie Humanoïde

## Slide robotique humanoide

humanoide -> moins comprise

du coup, pour les robots humanoides on fait le design en même temps que le reste pour pas avoir de problèmes

Pour l’intro sur les robots humanoides, parler d’hrp2, dire comment ont le fait bouger
puis c’est trop énergivore

# Conclusion Partie Humanoïde

# Conclusion Générale



# Review

Parler des arbres dans l’intro, en disant qu’ils ne se déplacent pas.

> Ces robots à roues sont étudiés dans le monde académique depuis plusieurs décénies, et la théorie concernant leur
> modélisation et leur contrôle est largement mature. On peut d’ailleurs observer l’arrivée de ces robots mobiles sur le
image de la roue, contrainte non holonome, roulement sans glissements

slide classes de robots mobiles:
mettre que les schemas, faire apparaitre les noms des projets, commenter principalement ceux qui nous intéressent.

on ne dit pas que c’est à l’extérieur de la thèse
