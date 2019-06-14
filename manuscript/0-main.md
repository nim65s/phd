---
title: Génération de mouvement en robotique mobile et humanoïde
author: Guilhem Saurel
institute: LAAS-CNRS
lang: fr
documentclass: book
papersize: A4
bibliography: bibliography.bib
link-citations: true
figPrefix:
- figure
- figures
eqnPrefix:
- équation
- équations
tblPrefix:
- table
- tables
lstPrefix:
- code source
- codes sources
secPrefix:
- section
- sections
listingTitle: Code source
lofTitle: Table des Figures
lotTitle: Table des Tables
lolTitle: Table des Codes sources
loaname: Table des Algorithmes
toc: true
lot: true
lof: true
loa: true
lol: true
cref: true
codeBlockCaptions: true
linkcolor: blue
citecolor: red
urlcolor: red
toccolor: blue
tlsphd: true
tlsphded: EDSYS-Robo
tlsphdets: INSA
defencedate: 3 octobre 2017
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
  name: Brigitte D'Andrea-Novel
  title: Professeur
  status: Rapporteur
- n: 2
  name: Christine Chevallereau
  title: Directeur de Recherche
  status: Rapporteur
- n: 3
  name: Guy Caverot
  title: Ingénieur, Ph.D.
  status: Examinateur
- n: 4
  name: Philippe Souères
  title: Directeur de Recherche
  status: Examinateur
- n: 5
  name: Michel Taïx
  title: Maître de Conférences
  status: Examinateur
- n: 6
  name: Jean-Paul Laumond
  title: Directeur de Recherche
  status: Directeur de thèse
flipbook: flipbook/img
flipbookmargin: 0.5cm
section-titles: false
monofont: Source Code Pro
mainfont: Source Han Serif JP
nocite: |
  @saurel16, @transhumus, @buondonno17
...

\renewcommand{\thepart}{\Roman{part}}
\renewcommand{\thechapter}{\Alph{chapter}}

\input{manuscript/partend}

\makeatletter
\renewcommand{\ALG@name}{Algorithme}
\makeatother
\algnewcommand\Ands{\;\textbf{and}\;}
\algnewcommand\Ors{\;\textbf{or}\;}

\newcommand{\vectwo}[2]{\ensuremath{\left(\begin{array}{c}{#1} \\ {#2}\end{array}\right)}}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
