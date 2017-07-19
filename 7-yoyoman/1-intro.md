## Robots bipèdes {#sec:yoyoman}

Dans ce chapitre, nous présentons une méthode de codesign de marcheurs bipèdes, adaptée à l’étude et la fabrication de
robots dont la répartition des masses et le contrôle sont simultanément optimisés.

Nous générons donc un mouvement de locomotion par l’optimisation simultanée d’une conception mécanique et d’un
contrôleur associé.

###  Introduction

Les marcheurs passifs sont des robots bipèdes actionnés principalement par la gravité. Ils utilisent leur dynamique
naturelle pour avancer, mais ne peuvent pas rester dans un équilibre quasi-statique stable.

De tels systèmes mécaniques ont un excellent coût de transport (CoT). Ils permettent à la fois au bio-mécaniciens de
mieux comprendre le fonctionnement de la marche bipède, et aux créateurs de robots de fabriquer des robots humanoïdes
plus efficaces.

Dans ce chapitre, nous proposons une méthode dynamique générique pour optimiser à la fois le design mécanique d’un
robot et de son contrôleur en fonction d’un coût donné. Elle est décrite dans la [@fig:framework].

Cette méthode cherche à tirer parti de la dynamique d’un marcheur passif, tout en permettant de créer un robot pouvant,
au choix, être actionné activement ou passivement.

![Vue d’ensemble de l’implémentation de notre méthode de simulation et d’optimisation. Le simulateur est décrit dans la
[@sec:yoyosimu] et le solveur numérique dans la [@sec:yoyosolv].](tikz/framework.pdf){#fig:framework}

Cette méthode consiste à donner principalement une structure cinématique et une fonction de coût à un solveur
numérique. Celui-ci doit alors optimiser les paramètres mécaniques du robot et de son contrôleur. Pour cela, il
utilise une librairie de calculs dynamiques pour simuler la réponse du système en fonction des paramètres et contrôles
qu’il lui donne.

#### Travaux apparentés

Depuis @mcgeer90, de nombreux marcheurs passifs ont été pensés et fabriqués. Une bonne introduction à ce
domaine est donnée par @collins05.

Une méthodologie complète de fabrication de marcheurs passifs de complexités croissantes et décrite par @wisse07.
Elle commence avec un simple modèle de compas (c’est à dire seulement un segment rigide pour chaque jambe, reliés par
une liaison pivot au niveau du bassin) et va jusqu’à la réalisation de Denise, un marcheur dynamique 3D, avec un
système d’équilibre du torse utilisant la bissectrice de l’angle des jambes, deux bras mécaniquement couplés aux angles
des hanches, des genoux que se déverrouillent pendant la phase de balancier, et des chevilles conçues pour diriger le
robot dans la direction qui empêche la chute.

Cette approche incrémentale révèle les principaux problèmes de la création de marcheurs anthropomorphes. Le premier de
ces problèmes est la transition du compas évoluant uniquement dans le plan sagittal (c’est à dire le plan de symétrie
pour un humanoïde) à un système 3D [@collins01;@tedrake04;@hobbelen08].

Le second problème est l’extension du modèle du compas à l’utilisation de jambes articulées
[@mcgeer90;@collins01;@ikemata06;@westervelt07;@hobbelen08].

Ensuite, l’ajout des chevilles est abordé dans [@wisse06;@hobbelen08], celui des bras dans [@tedrake04;@hobbelen08], et
celui du cou et de la tête dans [@benallegue13;@falotico16].

La distribution des masses pour une structure cinématique donnée est également un problème important, et il est
adressé dans [@hass06;@remy11].

Outre ces contributions mécatroniques, la recherche s’intéresse également à la minimisation de la consommation
énergétique [@collins05;@bhounsule14] et à la stabilité de marcheurs passifs
[@mombaur01;@grizzle01;@ikemata06;@byl09;@benallegue13].

Par opposition aux approches de contrôle prédictif non-passif [@kajita03;@pratt06] qui exigent une planification des
pas à l’avance, le contrôle de marcheurs passifs cherche à maintenir au mieux la dynamique périodique naturelle
provenant du design mécanique.

Le design mécanique et le contrôle sont profondément liés, et le défi est de les gérer tous les deux simultanément, en
considérant que le cycle limite provenant du design mécanique est à l’origine d’une démarche stable.

Le rôle du contrôleur est alors de maintenir au mieux le système proche de son cycle limite intrinsèque en dépit des
perturbations.

Dans le cas de l’optimisation fondée sur un modèle, la recherche d’un bon contrôleur est exprimé comme
un problème d’optimisation numérique contraint bénéficiant d’une solide analyse théorique de la stabilité [@diehl09].
Cette méthode numérique générale a été appliquée à la distribution des masses de marcheurs passifs [@hass06], puis
à l’étude de quadrupèdes passifs [@remy10], et enfin aux marcheurs passifs dans le cadre de la création et de l’analyse
de démarches efficaces [@remy11].

Dans ce dernier article, les auteurs proposent un système de simulation dynamique dont la portée est illustrée dans
divers exemples dont des marcheurs passifs et des robots qui courent. Notre travail utilise la même idée générale.

#### Définition du problème

Comme nous l’avons vu, notre but est de résoudre simultanément les deux problèmes suivants:

1. Pour une chaîne cinématique donnée, nous cherchons à optimiser les paramètres d’un robot tels que la distribution de
   masse, les longueurs des différents segments, la taille et la durée d’un pas, *etc.*;
2. Pour un robot donné, nous voulons le contrôleur minimisant au mieux une fonction de coût donnée, telle que le coût
   de transport, ou le temps minimal.

En bref, pour une structure cinématique donnée, nous proposons une méthode générique pour trouver tous les paramètres
d’un robot ainsi que le contrôleur qui optimisent une fonction de coût donnée.

#### Contributions

La première nouveauté de cette approche est sa capacité à gérer une architecture complexe telle qu’un marcheur
humanoïde, tant en 2D qu’en 3D. Il n’est pas nécessaire que le mouvement se fasse uniquement dans le plan sagittal.

De plus, et contrairement aux travaux similaires sur le sujet, notre système calcule automatiquement la dynamique
complète d’un robot donné. Il n’est donc plus nécessaire de décrire entièrement un système polyarticulé à travers ses
équations dynamiques. De ce fait de nombreux marcheurs passifs peuvent être efficacement créés, optimisés et comparés.

Deuxièmement, le contrôle peut être actif ou passif. Tout type d’actionneur peut être modélisé et géré par cette
méthode. Nous pouvons par exemple appliquer un couple idéal suivant une spline, déterminer les coefficients d’un
ressort ou d’un amortisseur, ou encore utiliser des moteurs en série ou en parrallèle avec des ressorts.

On peut également gérer une démarche périodique ou non-périodique.

Enfin, nous pouvons optimiser différents paramètres d’un marcheur donné (pente, longueurs, masses, vitesses, *etc.*)
par rapport à une fonction de coût donnée.

#### Plan

Dans la [@sec:yoyosimu], nous commençons par introduire le simulateur de contacts dynamiques au cœur du système. Nous
montrons comment les différents paramètres du problème sont répartis entre le modèle mécanique et le contrôleur.

Dans la [@sec:yoyosolv], nous établissons la formulation générique de contrôle optimal qui permet l’optimisation de ces
paramètres.

Ensuite, nous présentons un protocole expérimental visant à illustrer notre méthode dans la [@sec:exptest], dont les
résultats sont donnés dans la [@sec:restest].
