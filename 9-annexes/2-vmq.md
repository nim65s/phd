## Implémentation logicielle pour le projet *transhumus* {#sec:anntranshumus}

Comme nous l’avons vu dans la [@sec:transarchi], nous avons utilisé la bibliothèque logicielle ZeroMQ comme base de
notre architecture logicielle.

Cette architecture modulaire peut être schématisée suivant la [@fig:modules]:

![Modules de l’architecture logicielle du projet *transhumus*](tikz/modules.pdf){#fig:modules width=100%}

Le composant principal de cet architecture est donc le générateur de trajectoires. Il ouvre à a fois un *socket* de
type *Pull* pour que d’autres modules puissent lui envoyer des données, et un *socket* de type *Pub* pour publier les
données aux modules qui en ont besoin.

Ainsi, tous les autres composants se connectent grâce à un composant de type *Push* au *socket Pull* et/ou un composant
de type *Sub au *socket PUB*, et peuvent donc être ajoutés, enlevés et rechargés à la volée. Chaque composant peut
ainsi traiter chaque information à son rythme, être codé dans n’importe quel langage et être éxécuté sur n’importe quel
ordinateur.

Pour simplifier les choses nous n’utilisons que des données sérialisables au format JSON.  Par exemple, dans notre cas,
le dictionnaire des données à traiter pour chaque AGV est donné dans le [@lst:data].

```{#lst:data .python}
DATA = {
    # Status:
    'status': 'Not connected', 'errors': 'Not connected', 'anomaly': False,
    'is_up': False, 'inside': False, 'last_seen_agv': str(datetime(1970, 1, 1)),
    # Position:
    'x': 0, 'y': 0, 'a': 0,
    # Vitesse:
    'v': 0, 'w': 0, 't': 0,
    # Vitesse à atteindre
    'vg': 0, 'wg': 0, 'tg': 0,
    # Vitesses et orientations des tourelles à atteindre:
    'vt': [0, 0, 0], 'tt': [0, 0, 0],
    # Vitesses et orientations des tourelles de consigne pour l'AGV:
    'vc': [0, 0, 0], 'tc': [0, 0, 0],
    # Vitesses et orientations des tourelles réelles lues sur l'AGV:
    'vm': [0, 0, 0], 'tm': [0, 0, 0],
    # Nombre de tour des tourelles
    'nt': [0, 0, 0],
    # Valeurs absolues des sondes graniers et normalisation
    'granier': [0] * N_PROBES, 'gm': [10] * N_PROBES,
    'gmi': [-10] * N_PROBES, 'gma': [0] * N_PROBES,
    # Commandes
    'stop': False, 'smoothe': False, 'smoothe_speed': True, 'boost': False,
    # Destination et état (cf. l'algorithme |D-3|):
    'destination': [0, 0], 'state': -1,
}
```

: Valeurs initiales des données utilisées par chaque AGV

### Composants

#### Composants abstraits de base

`VMQ` est le composant servant de base à tous nos modules.

```{.python include=venise/transhumus/vmq/vmq.py}
```
