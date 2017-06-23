#!/usr/bin/env fish

while inotifywait **.md
    sleep .5
    pandoc -N --top-level-division=part -F pandoc-crossref -F pandoc-citeproc -F filters/subfigs.py -o phd.pdf **.md
end
