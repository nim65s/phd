### Étude d’actionneurs {#sec:sea}

Dans cette section, nous adaptons notre méthode aux actionneurs composés d’un moteur et d’un ressort, montés en série
ou en parallèle.

Les *Series Elastic Actuators* (SEA) [@pratt95] représentent une nouvelle génération d’actionneurs en ajoutant un
élément d’une élasticité non négligeable entre un moteur et le segment qui lui est associé.

Ces actionneurs ont déjà été utilisés sur des robots humanoïdes [@tsagarakis13]. Ils peuvent en améliorer les
performances, notamment au niveau de la gestion des impacts, de l’efficacité énergétique, et de la sécurité à la fois
pour le robot et les humains.

Les *Parallel Elastic Actuators* (PEA) [@grimmer12] sont quant à eux utiles pour emmagasiner de l’énergie, et ainsi
réduire les pics de puissance consommée.

Nous comparons donc les cas suivants:

- Actionneurs:
    - moteurs rigides;
    - moteurs et ressorts en série;
    - moteurs et ressorts en parallèle;
- Modèles:
    - Compas 2D $M_A$;
    - Corps complet 3D $M_E$;
- Fonction de coût:
    - Coût de transport;
    - Norme au carré du couple.

#### État du système

Dans le cas de moteurs rigides ou de moteurs et ressorts montés en parallèle, l’état du système est défini par les
positions et vitesses angulaires des articulations, comme le montre l’[@eq:psa]

$$ \mathbf x = \left(\mathbf q^\top \mathbf{\dot q}^\top\right)^\top $$ {#eq:psa}

Cependant, dans le cas d’actionneurs série élastiques, la position angulaire d’un moteur ne suffit pas pour avoir la
position angulaire de l’articulation. On a donc besoin de considérer à la fois la position angulaire du moteur (après
un éventuel réducteur), que l’on note $\theta$ et celle de l’articulation, qui reste notée $q$. Cela nous donne donc
l’[@eq:esa].

$$ \mathbf x = \left(\mathbf q^\top \mathbf{\dot q}^\top \mathbf\theta^\top \mathbf{\dot\theta}^\top\right)^\top $$ {#eq:esa}

Naturellement, comme précédemment, nous utilisons un seul jeu de paramètres qualifiant un ressort donné pour une paire
d’articulations symétriques.

#### Fonctions de coût

L’expression du coût de transport est légèrement modifiée, comme le montre l’[@eq:esacot].

$$ c_{\text{CoT}} = \int\limits_{t=0}^T\cfrac{|\mathbf\tau|^\top|\mathbf{\dot\theta}|}{d}dt $$ {#eq:esacot}

On notera que, contrairement aux expériences précédentes, ce coût de transport n’est pas le coût de transport sans
unités classique. Celui-ci s’exprime en Watts par mètre.

Dans un second lot d’expériences, nous utilisons plutôt le carré de la norme du couple, normalisé par la longueur d’un
pas, selon l’[@eq:snt]. Cette fonction est utile pour limiter l’énergie dépensée par les moteurs, et @schultz10 ont
montré que cela pouvait produire des comportements semblant plus naturels.

$$ c_{\mathbf\tau} = \int\limits_{t=0}^T\cfrac{\|\mathbf\tau\|^2}{d}dt $$ {#eq:snt}

#### Expériences

Dans cette section, nous présentons les expériences menées sur l’optimisation de marcheurs de deux modèles, utilisant
trois types d’actionneurs, séparées en deux tables selon la fonction de coût utilisée. Ces résultats sont également
disponibles en vidéo[^13].


              ![](imgs/tfw.png){height=2cm} ![](imgs/tew.png){height=2cm} ![](imgs/tpw.png){height=2cm} ![](imgs/tff.png){height=4cm} ![](imgs/tef.png){height=4cm} ![](imgs/tpf.png){height=4cm}
------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- -----------------------------
Modèle        $M_A$                         $M_A$                         $M_A$                         $M_E$                         $M_E$                         $M_E$
Actionneurs   Rigide                        Série                         Parallèle                     Rigide                        Série                         Parallèle
Coût [N²m]    0.09563                       0.00004                       0.00060                       0.62844                       0.12800                       0.36654
Longueur [m]  0.6                           0.92726                       0.65017                       0.6                           0.6                           0.6
Durée [s]     0.74361                       0.90204                       0.73318                       0.64572                       0.81010                       0.51664
Vitesse [m/s] 0.80687                       1.02795                       0.88679                       0.92919                       0.74065                       1.16135
------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- -----------------------------
: Expériences utilisant une fonction de coût $c_{\mathbf\tau}$. {#tbl:tau}


              ![](imgs/cfw.png){height=2cm} ![](imgs/cew.png){height=2cm} ![](imgs/cpw.png){height=2cm} ![](imgs/cff.png){height=4cm} ![](imgs/cef.png){height=4cm} ![](imgs/cpf.png){height=4cm}
------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- -----------------------------
Modèle        $M_A$                         $M_A$                         $M_A$                         $M_E$                         $M_E$                         $M_E$
Actionneurs   Rigide                        Série                         Parallèle                     Rigide                        Série                         Parallèle
Coût [W/m]    0.45729                       0.04651                       0.03863                       0.51831                       0.00844                       0.04792
Longueur [m]  0.91416                       0.78682                       0.69466                       0.6                           0.6                           0.85526
Durée [s]     0.80094                       0.87833                       0.61705                       0.59480                       0.82184                       0.47053
Vitesse [m/s] 1.14136                       0.89581                       1.12577                       1.00875                       0.73007                       1.81764
------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- ----------------------------- -----------------------------
: Expériences utilisant une fonction de coût $c_{\text{CoT}}$. {#tbl:cot}


<!-- a_ -->

[^13]: [http://homepages.laas.fr/gsaurel/iros.mp4](http://homepages.laas.fr/gsaurel/iros.mp4)

<!--TODO: update this link for hal.laas.fr-->

#### Résultats

Les douze expériences présentées dans les [@tbl:tau;@tbl:cot] illustrent une nouvelle fois le potentiel
et l’utilité de notre méthode.

Naturellement, ces résultats comparatifs ne sont pas encore suffisants pour affirmer qu’un critère est plus important à
optimiser qu’un autre, ou qu’un type d’actionneur est meilleur qu’un autre en général.

Cependant, ces expériences nous permettent de faire plusieurs remarques en les comparant.

Dans un premier temps, on observe effectivement que les marcheurs corps complet ont des démarches semblant plus
naturelles pour $c_{\mathbf\tau}$ que pour $c_{\text{CoT}}$, et notamment sur la vidéo.

Ensuite, on constate systématiquement que le coût est inférieur pour les actionneurs aidés de ressorts que pour les
actionneurs rigides.

Aussi, si l’on compare les actionneurs en série ou en parallèle avec des ressorts, on observe des oscillations
rapides dans le premier cas et pas le second. En d’autres termes, il semble que dans les cas étudiés ici, les SEA
stressent plus fortement les arbres des moteurs, ce qui pourrait éventuellement s’avérer néfaste. Ce comportement n’est
pourtant pas étonnant, dans la mesure où la solution optimale n’est pas forcément lisse. De plus, un comportement
oscillatoire est typique des SEAs.

Enfin, on note contre-intuitivement qu’il ne semble pas y avoir de corrélation dans ces expériences entre la vitesse de
déplacement et le coût. Ceci pourrait par exemple nous permettre de concevoir des robots à la fois rapides et économes
en énergie, en prenant en compte la vitesse dans la fonction de coût [@chevallereau01].
