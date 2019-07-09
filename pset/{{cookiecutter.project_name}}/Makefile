
LATEXMK = latexmk
BASENAME = {{ cookiecutter.file_name }}

all: doc solutions

doc : $(BASENAME).tex
	$(LATEXMK) -pdf -pdflatex='lualatex %O --shell-escape  \
	-interaction=nonstopmode -synctex=1 %S' $(BASENAME).tex

solutions : $(BASENAME).tex
	$(LATEXMK) -pdf -pdflatex='lualatex %O --shell-escape \
	 -interaction=nonstopmode -synctex=1 \
	 "\PassOptionsToClass{solutions}{worksheet}\input{{ '{%S}' }}"' \
	 -jobname="$(BASENAME)-solutions" $(BASENAME).tex

clean :
	$(LATEXMK) -silent -c $(BASENAME).tex
	$(LATEXMK) -silent -c -jobname=$(BASENAME)-solutions

.PHONY : all doc solutions clean