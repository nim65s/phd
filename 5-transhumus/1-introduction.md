## Robots mobiles tri-tourelles {#sec:transhumus}

Dans ce dernier chapitre sur la robotique mobile, nous faisons le rapport d’un projet réalisé pour l’Institut Français,
en coopération avec les entreprises BA Systèmes et Ubisense. Il a consisté a implémenter le contrôle et la
planification de robots mobiles omnidirectionnels.

Comme pour le projet *offroad* présenté dans le chapitre [-@sec:offroad], les robots constituent une œuvre d’art de
l’artiste Céleste Boursier-Mougenot. Cette fois-ci, nous dottons de moyens de locomotion trois pins sylverstres, de
plusieurs mètres de haut et plusieurs tonnes.


### Introduction

La Biennale de Venise [@DiMartino] est la plus importante exposition internationnale d’art contemporain. Elle a lieu
une fois tous les deux ans depuis 1895. L’exposition est répartie dans différents lieux à Venise, parmis lesquels les
*Giardinni* comportant 90 pavillons étant chacun dirigés par une nation.

Pour la 56^ième^ édition en 2015, l’Institut Français, en charge du pavillon français, a choisi le projet
Rêvolutions de Céleste Boursier-Mougenot. Ce projet incluait l’œuvre transHumUs dont nous parlons dans ce chapitre.

Dans transHumUs, l’artiste a voulu extraire une chorégraphie de trois arbres mobiles se déplançant en fonction de leur
métabolisme, c’est à dire là variation du flux de leur sève losqu’ils passent de l’ombre à la lumière.
Ce spectacle a eu lieu de mai à novembre, six jours par semaine, huit heures par jour.

La [@fig:transhumusintro] présente respectivement l’idée initiale et la réalisation finale du projet. Neuf mois
séparent les deux images.  L’objectif de ce chapitre est de faire le rapport sur la recherche et le développement qui
ont été conduits pendant cette période, depuis notre première réunion avec l’artiste jusqu’au vernissage de
l’exposition le 5 main 2015.

<div id="fig:transhumusintro">
![Vue d’artiste](imgs/dessin.png){height=4.5cm}
![Résultat final](imgs/couverture.jpg){height=4.5cm}

Des spécifications à la réalisations. Neuf mois séparent les deux images.
</div>

Comment transcrire la dimension poétique de ce projet en des termes technologiques ? La question s’addresse à tous les
composants d’un système robotique, de la conception de machines capables de déplacer trois tonnes (l’arbre, l’arbre,
ses racines, et la terre nécessaire), l’architecture de perception qui doit combiner des capteurs egocentriques et
allocentriques, et le système de génération de mouvement qui doit retranscrire le critère de qualité du mouvement
défini par l’artiste en termes de de lissage de trajectoire et de vitesses.
