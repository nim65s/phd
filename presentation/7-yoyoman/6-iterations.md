#### Itérations

Le solveur propose ces paramètres au simulateur:

------------- -------------------------------------------
État          $\bm q$, $\bm{\dot q}$
Contrôle      $\bm \tau$
Démarche      longueur et durée d’un pas
Design        longueurs, masses, inerties des segments
Environement  texture et pente du sol
------------- -------------------------------------------

Le simulateur calcule alors $\bm{\ddot q}$ et l’intègre dans $\bm{\dot q}$ & $\bm q$.
