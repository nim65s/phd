# Ma thèse

# Get dependencies

- pandoc pandoc-crossref pandoc-citeproc pandoc-include-code
- https://github.com/nim65s/pandoc-templates.git

# Manuscript

```
pandoc -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code -F filters/subfigs.py -N \
    --top-level-division=part -B manuscript/before.tex --pdf-engine=lualatex --highlight-style=kate \
    -o phd.pdf manuscript/**.md
```
## Présentation

```
pandoc -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code -F filters/videos.py -N --toc \
    -t beamer --pdf-engine=lualatex --highlight-style=kate --slide-level=4 \
    -o slides.pdf --template=default presentation/**.md
```
