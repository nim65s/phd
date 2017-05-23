#!/usr/bin/env fish

while inotifywait **.md
    sleep .5
    pandoc -N --top-level-division=part -F pandoc-crossref -F pandoc-citeproc -o phd.pdf **.md
end
