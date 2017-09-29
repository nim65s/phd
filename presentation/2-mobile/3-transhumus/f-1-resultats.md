#### Résultats

%[](videos/venise.mp4)

<div class="notes">

Ce projet a été livré à temps pour l’ouverture de la 56ième Biennale de Venise, et a fonctionné six jours sur sept
pendant sept mois. Durant cette période, les principaux problèmes que nous avons rencontrés ont été la stabilité du sol
de l’esplanade, notamment en cas de fortes pluies. Nous avons aussi eu des problèmes de géolocalisation, causés par une
mauvaise configuration des filtres fournis par Ubisense, ce qui a rapidement été résolu par un ingénieur de leur
support technique.

Un second problème que nous avons rencontré concerne le choix initial de la classe du robot. Comme nous l’avons vu,
notre méthode de contrôle garanti l’unicité du CIR, et les échelles de temps couplées à un lissage rendent les
réorientations des tourelles très lisses. Cependant, il peut arriver que ce CIR se place au niveau d’une tourelle, et
on tombe alors dans un point singulier. Nous avons donc mis en place une contrainte supplémentaire pour éviter que ce
cas se produise. Une meilleure solution aurait été d’utiliser une autre classe de robots mobiles non soumise à ce
problème.

Cette œuvre sera à nouveau exposée très prochainement au MONA de Tasamanie. Nous avons déjà formé le personnel de ce
musée, et modifié certains détails pour adapter la génération de mouvement aux contraintes de ce nouveau lieu.

</div>
