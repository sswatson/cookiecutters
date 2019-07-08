
BASENAME={{ cookiecutter.file_name }}

all: $(BASENAME).tex
	latexmk -pdf -pdflatex='lualatex %O --shell-escape -interaction=nonstopmode -synctex=1 "\PassOptionsToClass{solutions}{worksheet}\input{{ '{%S}' }}"' -jobname="$(BASENAME)-solutions" $(BASENAME).tex
	latexmk -pdf -pdflatex='lualatex %O --shell-escape -interaction=nonstopmode -synctex=1 %S' $(BASENAME).tex
	latexmk -c $(BASENAME).tex
	latexmk -c -jobname=$(BASENAME)-solutions