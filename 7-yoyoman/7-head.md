### Étude de la stabilisation de la tête {#sec:head}

Dans cette section, nous ajoutons à notre méthode un mécanisme de simulation d’une centrale inertielle incorporée au
robot lui permettant de mieux se stabiliser.

Dans le cadre du projet Yoyo-Man [@yoyoman], il est intéressant d’étudier l’effet de la stabilisation de la tête sur la
locomotion bipède.

Dans ce but, nous avons implémenté dans notre cadre logiciel un estimateur de position de la tête imitant le système
vestibulaire humain suivant @farkhatdinov11.

Il suffit ensuite d’ajouter un terme dans la fonction de coût visant à minimiser l’angle entre cet estimateur et la
verticale, suivant l’[@eq:tete].

$$ c_\beta = c_{\text{CoT}} + K_\beta \beta $$ {#eq:tete}

Dans l’[@eq:tete], $\beta$ est l’angle mesuré entre le pendule inversé reproduisant le système vestibulaire humain et
la verticale, et $K_\beta$ un poids indiquant l’importance de l’objectif de la stabilisation de tête par rapport à
l’objectif $c_{\text{CoT}}$, que l’on pourrait également remplacer par $c_{\bm\tau}$.

La [@fig:tete] présente l’un des premiers résultats de démarche que l’on obtient dans ce cas.

![Marcheur bipède à quatre segments, articulé par deux hanches et un cou. La fonction de coût incorpore un objectif de
stabilisation verticale de l’estimateur du système vestibulaire. Le marcheur adopte ici une stratégie consistant à
lancer sa jambe en arrière pour mieux profiter de son inertie.](imgs/tete.png){#fig:tete height=7cm}
