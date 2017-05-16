# Ma thèse

# Build it:

`pandoc -N --top-level-division=part --filter pandoc-citeproc --metadata link-citations=true --latex-engine=xelatex -o phd.pdf **.md`

# Automate build:

`./watch.fish`
