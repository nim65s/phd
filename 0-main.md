---
title: Génération de mouvement en robotique mobile et humanoïde
author: Guilhem Saurel
institute: LAAS-CNRS
lang: fr
documentclass: book
papersize: A4
bibliography: bibliography.bib
link-citations: true
figPrefix: figure
eqnPrefix: équation
tblPrefix: table
secPrefix: section
lofname: Liste des Figures
lotname: Liste des Tables
loaname: Liste des Algorithmes
toc: true
lot: true
lof: true
loa: true
tlsphd: true
tlsphded: EDSYS-Robo
tlsphdets: INSA
defencedate: 29 septembre 2017
lab: Laboratoire d’Analyse et d’Architecture des Systèmes LAAS-CNRS
nboss: 1
nreferee: 2
njudge: 6
boss: Jean-Paul Laumond
referee:
- n: 1
  name: Brigitte D'Andrea-Novel
- n: 2
  name: Christine Chevallereau
judge:
- n: 1
  name: Philippe Souères
  title: Directeur de Recherche
  status: Président du Jury
- n: 2
  name: Brigitte D'Andrea-Novel
  title: Professeur
  status: Membre du Jury
- n: 3
  name: Christine Chevallereau
  title: Directeur de Recherche
  status: Membre du Jury
- n: 4
  name: Jean-Paul Laumond
  title: Directeur de Recherche
  status: Membre du Jury
- n: 5
  name: Michel Taïx
  title: Maître de Conférences
  status: Membre du Jury
- n: 6
  name: Guy Caverot
  title: Ingénieur, Ph.D.
  status: Invité
...

\renewcommand{\thechapter}{\Alph{chapter}}
\renewcommand{\theequation}{\Alph{chapter}-\arabic{equation}}

\makeatletter
\renewcommand{\ALG@name}{Algorithme}
\makeatother
\algnewcommand\Ands{\;\textbf{and}\;}
\algnewcommand\Ors{\;\textbf{or}\;}

\newcommand{\vectwo}[2]{\ensuremath{\left(\begin{array}{c}{#1} \\ {#2}\end{array}\right)}}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\thepage}
\fancyhead[RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
