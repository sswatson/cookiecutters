
LATEXMK = latexmk
BASENAME = {{ cookiecutter.file_name }}

all : doc
doc : pdf
pdf : $(BASENAME).pdf

%.pdf : %.tex
	$(LATEXMK) -pdf -pdflatex='lualatex %O --shell-escape  \
	-interaction=nonstopmode -synctex=1 %S' $*

clean :
	$(LATEXMK) -silent -c

.PHONY : all doc pdf clean