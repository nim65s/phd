#!/usr/bin/env fish

while inotifywait manuscript/**.{md,tex}
    sleep .5
    time pandoc -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code -F filters/subfigs.py -N \
        --top-level-division=part -B manuscript/before.tex --pdf-engine=lualatex --highlight-style=kate \
        -o phd.pdf manuscript/**.md
end
