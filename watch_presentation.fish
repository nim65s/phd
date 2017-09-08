#!/usr/bin/env fish

while inotifywait presentation/**.{md,tex}
    sleep .5
    time pandoc -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code -F filters/videos.py -N --toc \
        -t beamer --latex-engine=lualatex --highlight-style=kate --slide-level=4 \
        -o slides.pdf presentation/**.md
end
