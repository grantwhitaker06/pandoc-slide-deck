[title]: <> (Slide Decks with Pandoc)
[author]: <> (Kyle Gwinnup)
[subtitle]: <> (Credit to <a href='https://github.com/braje'>github.com/braje</a> & <a href='http://johnmacfarlane.net/pandoc/'>Pandoc</a>)
[site]: <> (<a href='http://kgwinnup.github.io'>http://kgwinnup.github.io/</a>)
[transition]: <> (zoom)
[template]: <> (default)
[theme]: <> (beige)

-------------------------------------------------------------------

# How to use

0. Download <a href='http://johnmacfarlane.net/pandoc/'>Pandoc</a>
1. Fork this repo: <a href="https://github.com/kgwinnup/pandoc-slide-deck">pandoc slidedeck creator</a>
2. Use pandoc markdown and create your slides
3. ./build.py
4. Never use powerpoint again

------------------------------------------------------------------

# Passing parameters into templates

* Pandoc key/val pairs are passed into the corresponding `$<varname>$`
* Variables are defined using link labels at the top of the Markdown
  file
    + They will not show up in the document
    + I realize this is hacky, but necessary to keep Markdown integrity

------------------------------------------------------------------

# Themes and templates

* HTML templates are stored in templates/
* If no template variable is set, the default is used
* Reveal.js has several included themes
    + beige, default, moon, night, serif, simple, sky, solarized 
