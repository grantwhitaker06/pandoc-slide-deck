#!/usr/bin/python
import re
import subprocess

flags = "--standalone -t revealjs --section-divs --template=template.html --no-highlight"
variables = ""

with open("slides.md") as slides:
    lines = slides.readlines()
    v_list = []
    for line in lines:
        if "---" in line:
            break
        v_list.append(line)

for v in v_list:
    if len(v) > 2:
        key = (re.compile('.*?((?:[a-z][a-z]+))', re.IGNORECASE|re.DOTALL)).search(v).group(1)
        val = (re.sub('(\\[.*?\\])(:)(\\s+)(<)(>)(\\s+)(.)', '', v))[:-2]
        variables += "-M " + key + "=\"" + val.strip() + "\" "

command = "pandoc " + flags + " slides.md " + variables + " -o index.html"
print command
subprocess.call(command, shell=True)
