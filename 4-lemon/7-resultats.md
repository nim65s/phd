### Résultats {#sec:lemonres}

Dans le cadre de ce projet, nous avons développé des classes et méthodes spécifiques au problème posé, nous les avons
intégrées avec les classes et méthodes déjà disponibles dans HPP, puis nous avons réglé empiriquement les différents
paramètres afin d’obtenir des trajectoires le plus satisfaisantes possible sur les exemples fournis ainsi que des cas
d’école.

Le résultat est une programme qui dans la plupart de cas produit une trajectoire couvrant bien la surface à nettoyer,
mais qui souvent produit des trajectoires plus longues que nécessaire.

#### Limitations

Comme nous l’avons vu dans la [@sec:bordures], nous recherchons pour l’instant uniquement des segments de droite, voire
des arcs de cercles dont le rayon doit être connu à priori.

Cependant, dans certains cas où plusieurs petits segments sont proches les uns des autres, les transformées de Hough
peuvent rater des segments de droites pourtant évidents pour un humain.

<!--TODO: exemple petit pilier-->

Aussi, cette transformée de Hough implique un choix des paramètres de discrétisation $(N_\rho, N_\theta)$. Pour pouvoir
bien construire une carte, il est donc souvent nécessaire de bien comprendre la théorie de la transformée afin
d’adapter ces paramètres à une zone donnée.

Sans cela, en utilisant des paramètres par défaut, des points alignés peuvent se retrouver sur des droites différentes
pour la transformée. Cet effet peut être amplifié par le bruit inhérent à toute carte construite à l’aide de capteurs.

En conséquence, cela implique des situations difficilement compréhensible pour un observateur extérieur où le robot
balaye plusieurs fois la même bordure.
