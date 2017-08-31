#!/usr/bin/env fish

while inotifywait **.{md,tex}
    sleep .5
    time pandoc -N --top-level-division=part -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code \
        -F filters/subfigs.py -B before.tex --latex-engine=lualatex --highlight-style=zenburn -o phd.pdf **.md
end
