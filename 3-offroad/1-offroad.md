## Robots mobiles différentiels {#sec:offroad}

Dans ce chapitre préambule, nous faisons le rapport d’un projet de robotique réalisé juste avant le commencement de
cette thèse. Il a consisté à implémenter la génération de mouvements de robots mobiles différentiels. Ces robots sont
en réalité des pianos à queue, qui errent dans un musée.

### Introduction du projet *off road*

*Off road* est un projet robotique atypique, puisqu’il s’agit de la réalisation d’une œuvre artistique.

L’artiste, l’exposition et l’œuvre sont présentés dans la suite de cette section.

#### Céleste Boursier-Mougenot

Céleste Boursier-Mougenot ([@fig:celeste]) est un artiste plasticien, musicien et installationniste français.

![Céleste Boursier-Mougenot à la biennale de Venise en 2015](imgs/celeste.jpg){#fig:celeste height=3cm}

Il est notamment connu pour des œuvres comme *from here to ear* ([@fig:fromheretoear]), où le public voit un musée
transformé en volière abritant des dizaines de petits oiseaux, qui ont pour perchoir des guitares électriques
amplifiées disposées horizontalement pour les accueillir.

C’est donc en se baladant que le visiteur joue de la musique, puisqu’il fait s’envoler les oiseaux des cordes des
guitares. L’artiste qualifie alors sa musique de « vivante ».

Parmi ses œuvres, on retrouve également *clinamen* ([@fig:clinamen]), dans laquelle des bols blancs flottent dans une
piscine circulaire bleutée, au gré d’un léger courant.

En s’entrechoquant, les bols en porcelaine forment une mélodie dont la partition est finement réglée grâce au nombre et
à la taille des bols, ainsi que la force et la direction du courant.

On voit également sur la [@fig:clinamen] des bancs autour de la piscine, invitant le visiteur à prendre le temps de
s’assoir et à profiter de l’œuvre, ce qui, paradoxalement, est plutôt rare dans un musée. Cette idée, chère à
l’artiste, se retrouve dans d’autres de ses projets, comme *zombiedrones* ou *rêvolutions*.

<div id="fig:celeste-oeuvres">
![*from here to ear*: des oiseaux se perchent sur une guitare électrique
amplifiée](imgs/from-here-to-ear.jpg){#fig:fromheretoear height=4cm}
![*clinamen*: des bols de porcelaine s’entrechoquent dans une piscine suivant un courant
artificiel](imgs/clinamen.jpg){#fig:clinamen height=4cm}

Œuvres classiques de Céleste Boursier-Mougenot.
</div>

#### Perturbations

Du 31 janvier au 4 mai 2014, le musée des Abattoirs de Toulouse a organisé l’exposition *perturbations*
([@fig:perturbations]), qui a principalement présenté cinq œuvres de Céleste Boursier-Mougenot, dont deux inédites.

L’une de ces deux œuvres réalisées pour l’occasion s’intitulait *off road* ([@fig:offroad]), et consistait à doter de
locomotion trois pianos à queue.

<div id="fig:perturbations">
![*off road*: trois pianos à queue évoluent parmi le public.](imgs/offroad.jpg){#fig:offroad width=100%}

![*scanner*: un ballon sonde muni d’un micro erre grâce à un ventilateur parmi des hauts-parleurs, créant des effets
Larsen modulés.](imgs/scanner.jpg){height=3.5cm}
![*averses*: un détecteur de particules cosmiques déclenche l’envoi d’une salve d’eau sur une batterie depuis le
plafond.](imgs/averses.jpg){height=3.5cm}

![*zombiedrone*: une télévision où chaque image est soustraite à la précédente. La bande son est générée à partir de
l’image. Les visiteurs peuvent s’assoir et changer de chaînes.](imgs/zombiedrones.jpg){#fig:zombiedrone height=3.5cm}
![*U43*: un téléphone en bakélite noir de type U43 sonne lorsque le mot « fantôme » apparaît sur Google
News.](imgs/u43.jpg){height=3.5cm}

Œuvres de Céleste Boursier-Mougenot lors de l’exposition *perturbations* du musée des Abattoirs de Toulouse en 2014.
</div>

#### *Off road*

Dans cette œuvre, trois pianos à queue errent dans le musée.

Comme pour *clinamen*, les pianos s’entrechoquent de temps en temps ou heurtent les murs (généralement à faible
vitesse), faisant ainsi résonner leur table d’harmonie.

Et comme pour *from here to ear*, le public fait partie de l’œuvre, puisqu’il est invité, s’il l’ose, à errer parmi les
pianos. Ce faisant, il ignore que ces derniers peuvent décider de le fuir ou de le poursuivre, comme nous les verrons
par la suite, [@sec:potentiels].

Dans la suite de ce chapitre, nous détaillons la réalisation technique de cette œuvre, financée par le musée des
Abattoirs de Toulouse, dirigée par l’artiste, et réalisée, en trois mois seulement, par Vincent Angladon pour la
gestion de la vision par ordinateur, Guilhem de Gramont pour la mécanique, Korantin Auguste, Ken Hasselmann et moi-même
pour la robotique.

<!--TODO le mouvement c’est la vie cf jpl-->
