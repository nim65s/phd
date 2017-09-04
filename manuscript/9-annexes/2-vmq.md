## Implémentation logicielle pour le projet *transhumus* {#sec:anntranshumus}

Comme nous l’avons vu dans la [@sec:transarchi], nous avons utilisé la bibliothèque logicielle ZeroMQ comme base de
notre architecture logicielle.

Cette architecture modulaire peut être schématisée suivant la [@fig:modules]:

![Modules de l’architecture logicielle du projet *transhumus*](tikz/modules.pdf){#fig:modules width=100%}

Le composant principal de cet architecture est donc le générateur de trajectoires. Il ouvre à a fois un *socket* de
type *Pull* pour que d’autres modules puissent lui envoyer des données, et un *socket* de type *Pub* pour publier les
données aux modules qui en ont besoin.

Ainsi, tous les autres composants se connectent grâce à un composant de type *PUSH* au *socket PULL* et/ou un composant
de type *SUB* au *socket PUB*, et peuvent donc être ajoutés, enlevés et rechargés à la volée. Chaque composant peut
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

: Valeurs initiales des données utilisées par chaque AGV.

### Briques élémentaires des transferts de données

Dans cette section nous détaillons les briques élémentaires qui permettent de créer les bases des modules. Ceux-ci
seront présentés dans les sections suivantes.

```{#lst:vmq .python include=venise/transhumus/vmq/vmq.py}
```

: `vmq/vmq.py`: composant abstrait servant de base à tous les modules.

```{#lst:pub .python include=venise/transhumus/vmq/publisher.py}
```

: `vmq/publisher.py`: composant de base permettant de publier des données.

```{#lst:sub .python include=venise/transhumus/vmq/subscriber.py}
```

: `vmq/subscriber.py`: composant de base permettant de souscrire aux données envoyées par le publieur.

```{#lst:pull .python include=venise/transhumus/vmq/puller.py}
```

: `vmq/puller.py`: composant de base permettant de tirer des donnnées.

```{#lst:push .python include=venise/transhumus/vmq/pusher.py}
```

: `vmq/pusher.py`: composant de base permettant de pousser des donnnées vers le tireur.

### Composants de base

Dans cette section, nous présentons les bases servant à créer les modules vus dans la [@fig:modules], elles-même créees
à partir des composants de gestion des transferts de données vus dans la section précédente.

```{#lst:input .python include=venise/transhumus/inputs/input.py}
```

: `inputs/input.py`: base servant à créer des modules envoyant des données dans le système.

```{#lst:processor .python include=venise/transhumus/processors/processor.py}
```

: `processors/processor.py`: base servant à créer des modules capables de recevoir des données, de les traiter, et d’en
mettre à jour d’autres..

```{#lst:base_trajectory .python include=venise/transhumus/trajectories/base_trajectory.py}
```

: `trajectories/base_trajectory.py`: base servant à créer le module principal générant le mouvement des AGVs.

```{#lst:probe .python include=venise/transhumus/inputs/probe.py}
```

: `inputs/probe.py`: base servant à créer des modules correspondant à des sondes tout en vérifiant les
valeurs renvoyées.

### Composants finaux

Dans cette section, nous exposons une partie des composants finaux créés sur les bases vues dans les deux sections
précédentes

```{#lst:print .python include=venise/transhumus/outputs/print.py}
```

: `output/print.py`: module de sortie affichant régulièrement les données dans le terminal.

```{#lst:granier_serial .python include=venise/transhumus/inputs/granier_serial.py}
```

: `inputs/granier_serial.py`: module d’entrée permettant de lire les données renvoyées par les sondes Granier.

```{#lst:granier_random .python include=venise/transhumus/inputs/granier_random.py}
```

: `inputs/granier_random.py`: module d’entrée permettant de simuler des valeurs de sondes granier. On peut également
utiliser d’anciennes données en lisant les fichiers de logs vus dans le [@lst:granier_serial].

```{#lst:granier .python include=venise/transhumus/processors/granier.py}
```

: `processors/granier.py`: module processeur de données permettant de normaliser les valeurs lues par les sondes
Granier.

```{#lst:is_up .python include=venise/transhumus/processors/is_up.py}
```

: `processors/is_up.py`: module processeur vérifiant que l’AGV est correctement connecté au module principal,
permettant d’alerter les utilisateurs au besoin. Un système similaire fonctionne dans l’autre sens, permettant de
stopper l’AGV en cas d’anomalie sur le flux de données. Naturellement, il est nécessaire que les machines du réseau
soient synchronisées en NTP.


```{#lst:websockets .python include=venise/transhumus/processors/websockets.py}
```

: `processors/websockets.py`: module processeur convertissant les données transportées par ZeroMQ en Websockets et
vice-versa.

### Code source complet

La totalité du code utilisé pour ce projet, ainsi que des instructions permettant de lancer rapidement un simulateur
avec docker-compose, sont disponibles sur [https://github.com/nim65s/venise](https://github.com/nim65s/venise).
