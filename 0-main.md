---
author: Guilhem Saurel
institute: LAAS-CNRS
lang: fr
documentclass: book
toc: true
papersize: A4
bibliography: bibliography.bib
link-citations: true
...

\renewcommand{\thechapter}{\Alph{chapter}}
\renewcommand{\theequation}{\Alph{chapter}-\arabic{equation}}
\renewcommand{\listfigurename}{Liste des Figures}
\renewcommand{\listtablename}{Liste des Tables}
\renewcommand{\listalgorithmname}{Liste des Algorithmes}
\makeatletter
\renewcommand{\ALG@name}{Algorithme}
\makeatother
\algnewcommand\Ands{\;\textbf{and}\;}
\algnewcommand\Ors{\;\textbf{or}\;}

\newcommand{\vectwo}[2]{\ensuremath{\left(\begin{array}{c}{#1} \\ {#2}\end{array}\right)}}

\listoffigures
\listoftables
\listofalgorithms

