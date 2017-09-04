# Ma thèse

# Build it:

`pandoc -N --top-level-division=part -F pandoc-crossref -F pandoc-citeproc -F filters/subfigs.py -o phd.pdf **.md`

# Automate build:

`./watch.fish`
