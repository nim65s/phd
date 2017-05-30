SOURCES = $(wildcard *.tex)

all: $(SOURCES:%.tex=%.pdf)

%.pdf: %.tex
	pdflatex -shell-escape $< && pdfcrop $@ crop.pdf && mv crop.pdf $@

clean:
	-rm -vf *.aux *.log *.nav *.media *.snm *.toc *.tmp *.tns *.pyg *.vrb *~ *.orig *.gnuplot *.table *.fls *.fdb_latexmk *.blg *.bbl 2> /dev/null
