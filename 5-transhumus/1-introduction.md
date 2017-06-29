## Robots mobiles tri-tourelles {#sec:transhumus}

Dans ce dernier chapitre sur la robotique mobile, nous faisons le rapport d’un projet réalisé pour l’Institut Français,
en coopération avec les entreprises BA Systèmes et Ubisense. Il a consisté à implémenter le contrôle et la
planification de robots mobiles omnidirectionnels.

Comme pour le projet *offroad* présenté dans le chapitre [-@sec:offroad], les robots constituent une œuvre d’art de
l’artiste Céleste Boursier-Mougenot. Cette fois-ci, nous dotons de moyens de locomotion trois pins sylvestres, de
plusieurs mètres de haut et plusieurs tonnes.


### Introduction {#sec:transintro}

La Biennale de Venise [@DiMartino] est la plus importante exposition d’art contemporain au monde. Elle a lieu
une fois tous les deux ans depuis 1895. L’exposition est répartie dans différents lieux à Venise, parmi lesquels les
*Giardini* comportant 90 pavillons, étant chacun dirigés par une nation.

Pour la 56^ième^ édition en 2015, l’Institut Français, en charge du pavillon français, a choisi le projet
Rêvolutions de l’artiste Céleste Boursier-Mougenot et la commissaire Emma Lavigne. Ce projet incluait l’œuvre
transHumUs dont nous parlons dans ce chapitre.

Dans transHumUs, l’artiste a voulu créer une chorégraphie de trois arbres mobiles se déplaçant en fonction de leur
métabolisme, et a choisi la variation du flux de leur sève losqu’ils passent de l’ombre à la lumière.
Ce spectacle a eu lieu de mai à novembre, six jours par semaine, huit heures par jour.

La [@fig:transhumusintro] présente respectivement l’idée initiale et la réalisation finale du projet. Neuf mois
séparent les deux images.  L’objectif de ce chapitre est de faire le rapport sur la recherche et le développement qui
ont été conduits pendant cette période, depuis notre première réunion avec l’artiste jusqu’au vernissage de
l’exposition le 5 mai 2015.

<div id="fig:transhumusintro">
![Vue d’artiste](imgs/dessin.png){height=4.5cm}
![Résultat final](imgs/couverture.jpg){height=4.5cm}

Des spécifications à la réalisation. Neuf mois séparent les deux images.
</div>

Comment transcrire la dimension poétique de ce projet en des termes technologiques ? La question s’adresse à tous les
composants d’un système robotique, de la conception de machines capables de déplacer trois tonnes (l’arbre,
ses racines, et la terre nécessaire), l’architecture de perception qui doit combiner des capteurs égocentriques et
allocentriques, et le système de génération de mouvement qui doit retranscrire le critère de qualité du mouvement
défini par l’artiste en termes de lissage de trajectoire et de vitesse.

Notre contribution dans ce projet a été de sélectionner les fournisseurs ([@sec:transspecs]), développer un
architecture logicielle comprenant une interface-utilisateur pour l’équipe du pavillon ([@sec:transarchi]) et s’occuper
de la gestion du projet ([@sec:transresults]).

Notre seconde contribution a été de proposer à l’artiste des stratégies de génération et de planification du mouvement
donnant l’impression que les arbres errent en totale autonomie ([@sec:transplanif]).
