# Ma thèse

# Get dependencies

```
stack setup
git clone git@github.com:nim65s/pandoc.git
cd pandoc
stack install --test
cd
echo "extra-deps:" >> .stack/global-project/stack.yaml
echo "- roman-numerals-0.5.1.5" >> .stack/global-project/stack.yaml
stack install pandoc-crossref pandoc-citeproc pandoc-include-code
```

# Manuscript

## Build

```
pandoc -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code -F filters/subfigs.py -N \
    --top-level-division=part -B manuscript/before.tex --pdf-engine=lualatex --highlight-style=kate \
    -o phd.pdf manuscript/**.md
```
## Automate build

`./watch_manuscript.fish`

## Présentation

## Build

```
pandoc -F pandoc-crossref -F pandoc-citeproc -F pandoc-include-code -F filters/videos.py -N --toc \
    -t beamer --pdf-engine=lualatex --highlight-style=kate --slide-level=4 \
    -o slides.pdf --template=default presentation/**.md
```

## Automate build

`./watch_presentation.fish`
