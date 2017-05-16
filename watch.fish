#!/usr/bin/env fish

while inotifywait **.md
    sleep .5
    pandoc -N --top-level-division=part --filter pandoc-citeproc --metadata link-citations=true --latex-engine=xelatex -o phd.pdf **.md
end
