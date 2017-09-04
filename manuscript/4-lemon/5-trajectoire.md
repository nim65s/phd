### Génération de la trajectoire finale {#sec:trajectoirefinale}

Une fois que les trajectoires de balayage des bordures droites ([@sec:borduresdroites]) et courbes
([@sec:bordurescourbes]) ainsi que les trajectoires symétriques de nettoyage des surfaces ([@sec:surfaces]) sont
entrées dans la `Roadmap` sous forme de paires de configuration $(q_s, q_e)$, il reste à générer la trajectoire finale.

Pour cela, il faut commencer par déterminer l’ordre de parcours des trajectoires de balayage des bordures, puis celui
des trajectoires de nettoyage des surfaces. La trajectoire finale consiste alors à relier la suite de configurations
obtenue par des trajectoires dites de @reedsshepp, composées de segments de droites et d’arcs de cercles.

Dans le but de déterminer l’ordre de parcours des trajectoires, nous avons utilisé un algorithme glouton. Ainsi, à
partir de la position initiale du robot, nous recherchons la configuration de départ de la trajectoire de suivi
balayage des bordures la plus proche, au sens de la distance de Reeds and Shepp, et suivant la méthode de tir
aléatoire RRT-Connect de @rrt.

Ensuite, nous repartons de la configuration finale associée, et recommençons l’opération jusqu’à ce que toutes les
trajectoires de balayage des bordures soient effectuées. Le même procédé est alors répété à partir de la configuration
finale de la dernière trajectoire de balayage des bordures pour les trajectoires de nettoyage des surfaces.

Les principaux algorithmes de cette section, qui sont la planification d’une trajectoire de Reeds and Shepp ansi que la
méthode RRT-Connect, sont directement implémentés dans HPP.
