# Ma thèse

```bash
while inotifywait **.md
    sleep .5
    pandoc -N --top-level-division=part --latex-engine=xelatex -o these.pdf **.md
end
```
