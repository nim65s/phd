### Fabrication d’un prototype {#sec:proto}

L’étape suivant la simulation de robots est naturellement le prototypage physique. Dans cette section, nous décrivons
donc les travaux visant à fabriquer un robot réel, utilisant notre méthode d’optimisation.

Ce premier prototype a pour objectif d’étudier en situation réelle l’effet de la stabilisation de la tête par rapport à
la verticale, en suivant les concepts de la [@sec:tete]. Ce premier bipède doit rester le plus simple possible. Nous
utilisons donc un modèle composé de deux jambes, attachées au buste par des hanches à deux degrés de liberté. Le
premier permet à la jambe de se balancer d’avant en arrière, et le second permet de lever la jambe pour éviter qu’elle
heurte le sol au mauvais moment, de la même manière que ce qui a été réalisé par @bhounsule14, mais pour un bipède.

Deux bras sont également présents, et servent à contrecarrer le moment de lacet créé par le balancier des jambes. Et
bien sûr, un cou articulé vise à stabiliser la tête verticalement.

Les pieds sont arrondis, de manière à orienter la marche dans la direction qui empêche une chute latérale
[@wisse07denise], ainsi qu’à entretenir un mouvement de balancier.

<div id="fig:proto">
![Corps Complet](imgs/proto.png){height=9cm}
![Détail des hanches. Un degré de liberté en rotation est visible à l’avant, et un en translation à
l’arrière.](imgs/hanche.png){width=8cm}

Modèle CAD du prototype.
</div>
