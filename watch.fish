#!/usr/bin/env fish

while inotifywait **.{md,tex}
    sleep .5
    time pandoc -N --top-level-division=part -F pandoc-crossref -F pandoc-citeproc -F filters/subfigs.py -B before.tex --latex-engine=lualatex -o phd.pdf **.md
end
