
LATEXMK = latexmk
DOCNAME = {{cookiecutter.file_name}}

all: doc
doc: pdf
pdf: $(DOCNAME).pdf

%.pdf: %.tex
	$(LATEXMK) -pdf -pdflatex='lualatex %O --shell-escape  \
	-interaction=nonstopmode -synctex=1 %S' $*

clean:
	$(LATEXMK) -silent -c

.PHONY: all clean doc pdf