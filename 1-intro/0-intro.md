## Introduction Générale {-}

La robotique consiste à augmenter l’autonomie d’un système, en lui donnant des facultés de perception, de décision et
d’action.

Grâce à un savant mélange d’électronique, d’informatique, de mécanique, de mathématiques, d’intelligence artificielle,
d’automatique, et de bien d’autres domaines, elle a aujourd’hui bien dépassé le stade de science fiction, où elle était
encore il y a quelques décennies à peine.

En effet, la culture robotique est antérieure à ses applications industrielles et à la recherche qui y est associée. Le
terme robot lui-même trouve son origine en 1920 dans une pièce de théatre tchécoslovaque de Karel Čapek. Il y désigne
un automate travailleur universel, dans le sens où il pourrait éxécuter n’importe quelle tâche. Le premier automate
industriel qui ait vocation a être universel, Unimate, n’est apparu aux États-Unis que dans les années 1960.

Entre temps, Isaac Asimov a eu le temps d’introduire les «Trois lois de la robotique» dans ses romans de
science-fiction dès les années 1940. Puis, dans les années 1950, les enfants japonais ont à leur tour pu découvrir la
robotique avec le manga «Astro, le petit robot» d’Osamu Tezuka.

Ce manga a ensuite initié un nouveau genre, celui des «Mecha», mettant en scène des armures robotisées humanoïdes,
généralement utilisées au combat. De ce genre est par exemple issu l’univers de Gundam ([@fig:gundam]), une franchise
créée dans les années 1980 comportant entre autres des films, des romans, des mangas, des animés et des jouets, et
générant de nos jours annuellement environ 50 milliards de yens, soit 500 millions d’euros.

Parmis les artistes qui ont travaillé pour cette franchise, on retrouve le designer Yutaka Izubuchi, qui a également de
dessiné la première véritable plateforme de recherche en robotique humanoïde, HRP-2, financée par le programme japonais
«Humanoid Robotics Project».

Suite à une collaboration franco-japonaise, le LAAS-CNRS est le seul laboratoire à disposer d’une telle plateforme en
dehors du Japon, et ce depuis 2006: il s’agit d’HRP-2 14 ([@fig:hrp2]).

\newpage

<!--TODO: spécifier la hauteur des images-->

<div id="fig:japon">
![HRP-2 14, au LAAS-CNRS en 2015](imgs/hrp2.jpg){#fig:hrp2 width=42%}
![LM312V04 Victory Gundam, 1993](imgs/gundam.png){#fig:gundam width=54%}

Robots humanoïdes japonais, dans la recherche à gauche, et dans la fiction à droite.
</div>

De nos jours, on trouve des applications à la robotique dans tous les domaines de l’industrie, que ce soit pour la
fabrication, la manutention, ou le contrôle qualité. On la retrouve également dans un nombre croissant d’autres
secteurs, comme la médecine, l’agriculture, les transports, ou encore le spatial. En remplaçant ainsi de plus en plus
l’homme dans des tâches difficiles, répétitives, fastidieuses, voire dangereuses, elle démontre son impact sur la
société ainsi que son intérêt économique.

La robotique est intimement liée à la notion de mouvement. Le mouvement peut notamment servir à la manipulation, la
locomotion, ou à la communication. Dans cette thèse, nous nous intéresserons plus en détail à la locomotion. La
locomotion terrestre est généralement réalisée à l’aide de roues ou de chenilles, ou par un système bipède, ou encore
multipède.

Dans la partie [-@sec:mobile], nous étudierons la locomotion en robotique mobile, c’est-à-dire sur des robots à
roues, puis dans la partie [-@sec:humanoide] nous parlerons de robotique humanoïde et donc de locomotion bipède.
