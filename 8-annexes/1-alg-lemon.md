## Algorithmes complémentaires pour le projet LEMON {#sec:annlemon}

\begin{algorithm}
\caption{Liste des configurations $\bm\bar q$ suivant la droite $(\rho, \theta)$ orientée en $\sigma$}
\label{alg:line}
\begin{algorithmic}[1]
\Procedure{Line}{$\rho, \theta, \sigma$}

\State $S, E \gets \Call{findExtremities}{\rho, \theta}$
\Comment{\parbox[c]{.5\linewidth}{Début et fin de l’intersection de la droite $(\rho, \theta)$ et des bords du
\texttt{Bitmap}}}
\If{$\sigma < 0$}
\State $S, E \gets E, S$
\EndIf
\State $\bm{\bar q} \gets [(x, y, \sigma\theta) \forall (x, y) \in \operatorname{linspace}(S, E)]$
\State \textbf{return} $\bm{\bar q}$
\EndProcedure
\end{algorithmic}
\end{algorithm}


\begin{algorithm}
\caption{Recherche des extrémités $S, E$ de la droite $(\rho, \theta)$ sur le \texttt{Bitmap}}
\label{alg:extremites}
\begin{algorithmic}[1]
\Procedure{findExtremities}{$\rho, \theta$}

\If{$\sin(\theta) = 0$}
    \State $S \gets \vectwo{x_{min} + \rho}{y_{min}}$
    \State $E \gets \vectwo{x_{min} + \rho}{y_{max}}$
\ElsIf{$\cos(\theta) = 0$}
    \State $S \gets \vectwo{x_{min}}{y_{min} + \rho}$
    \State $E \gets \vectwo{x_{max}}{y_{min} + \rho}$
\Else
    \State $A \gets \vectwo{x_{min}}{ y_{min} + \cfrac{\rho }{ \sin(\theta)}}$
    \State $B \gets \vectwo{x_{min} + \cfrac{\rho }{ \cos(\theta)}}{ y_{min}}$
    \State $C \gets \vectwo{x_{max}}{ y_{min} + (\rho - (y_{max} - y_{min}) \operatorname{cotan}(\theta))}$
    \State $D \gets \vectwo{ x_{min} + \left(\rho - (x_{max} - x_{min}) \tan(\theta)\right)}{ y_{max}}$
    \State $start \gets false$

    \If{$y_{min} \leqslant y_A \leqslant y_{max}$}
        \State $start \gets true$
        \State $S \gets A$
    \EndIf

    \If{$x_{min} \leqslant x_B \leqslant x_{max}$}
        \If{$start$}
            \State $E \gets B$
        \Else
            \State $start \gets true$
            \State $S \gets B$
        \EndIf
    \EndIf

    \If{$y_{min} \leqslant y_C \leqslant y_{max}$}
        \If{$start$}
            \State $E \gets C$
        \Else
            \State $S \gets C$
        \EndIf
    \EndIf

    \If{$x_{min} \leqslant x_D \leqslant x_{max}$}
        \State $E \gets D$
    \EndIf

\EndIf

\State \textbf{return} $S, E$
\EndProcedure
\end{algorithmic}
\end{algorithm}
