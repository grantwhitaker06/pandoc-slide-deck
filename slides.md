[title]: <> (Slide Decks with Pandoc)
[author]: <> (Kyle Gwinnup)
[subtitle]: <> (Credit goes to <a href='https://github.com/braje'>github.com/braje</a> & <a href='http://johnmacfarlane.net/pandoc/'>Pandoc</a>)
[site]: <> (<a href='http://kgwinnup.github.io'>http://kgwinnup.github.io/</a>)
[transition]: <> (zoom)

-------------------------------------------------------------------

# How to use

0. Download <a href='http://johnmacfarlane.net/pandoc/'>Pandoc</a>
1. Fork this repo: <a href="#">pandoc slidedeck creator</a>
2. Use pandoc markdown and create your slides
3. Never use powerpoint again

-------------------------------------------------------------------

# Notes on usage

* Pandoc key/val pairs are passed into the coorisponding `$<varname>$`
* Variables are defined using link labels at the top of the Markdown
  file
    + They will not show up in the document
    + I realize this is hacky, but necessary to keep Markdown integrety

-------------------------------------------------------------------

## List example

* list item 1
* list item 2
* list item 3
    + sublist item

## Code example

```scala
//Simple Hello World 
object HelloWorld extends App{
  println("Hello World")
}
```
