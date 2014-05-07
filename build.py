#!/usr/bin/python
import re
import subprocess

default_variables = {'title': 'title goes here',
                     'author': 'author name',
                     'date': 'date here',
                     'subtitle': 'subtitle here',
                     'transition': 'zoom'}

default_flags = "--standalone -t revealjs --section-divs --no-highlight"

def readSlidesMd(f):
    with open(f) as slides:
        lines = slides.readlines()
        v_list = []
        for line in lines:
            if "---" in line:
                break
            v_list.append(line)

    return v_list

def parseVarsFromComments(v_list, variables):
    """returns a dictionary of all the variables defined at the top of your markdown slides"""
    for v in v_list:
        if len(v) > 2:
            key = (re.compile('.*?((?:[a-z][a-z]+))', re.IGNORECASE|re.DOTALL)).search(v).group(1)
            val = (re.sub('(\\[.*?\\])(:)(\\s+)(<)(>)(\\s+)(.)', '', v))[:-2]
            variables[key] = val.strip()

    return variables

def buildVariablesString(variables):
    """return a string with all the variables defined for pandoc including flags"""
    vstr = ""
    for key,val in variables.iteritems():
        vstr += "-M " + key + "=\"" + val + "\" "
    
    return vstr 

def templateStringParameter(template_value=None):
    if template_value:
        return " --template=templates/" + template_value + ".html "
    else:
        return " --template=templates/default.html "

def buildFlagsString(default_flags, variables):
    return default_flags + templateStringParameter(variables['template'])

def buildCommandString(flags, variables):
    return "pandoc " + flags + " slides.md " + variables + " -o index.html"

if __name__ == "__main__":
    unparsed_variables = readSlidesMd("slides.md")
    parsed_variables = parseVarsFromComments(unparsed_variables, default_variables)
    variable_string = buildVariablesString(parsed_variables)
    flags = buildFlagsString(default_flags, parsed_variables)
    command = buildCommandString(flags, variable_string)
    print command
    subprocess.call(command, shell=True)
