FLAGS=--standalone -t revealjs --section-divs --template=template.html --no-highlight

all: index.html

index.html: slides.md template.html Makefile
	pandoc $(FLAGS) $(VARS) slides.md -M title=$(TITLE) subtitle=$(SUBTITLE) author=$(AUTHOR) date=$(DATE) transition=$(TRANSITION) -o index.html

