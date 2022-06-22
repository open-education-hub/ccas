#!/usr/bin/python
import re
import sys

### TODO: fbox, $$non-whitespace

# This script modifies the raw CCAS.tex file to prepare it for conversion with pandoc

img_counter = 0

def replace_img(match):
    global img_counter
    img_counter += 1
    return "\\begin{picture}\n%s\n\\end{picture}\n" % img_counter

# Replace method for text and regex
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text

def process_fboxes(text):
    block_regex = re.compile(r'\\fbox\{')
    endblock_regex = re.compile(r'\}')
    block_stack = []
    resultlines = []
    for line in text.splitlines():
        match = block_regex.match(line)
        if match:
            # Starting a new block
            block_stack.append("fbox")
            resultlines.append("\\begin{fbox}")
        elif len(block_stack) > 0 and endblock_regex.match(line):
            block_stack.pop()
            resultlines.append("\\end{fbox}")
        else:
            resultlines.append(line)
    return '\n'.join(resultlines)

# Dictionaries with our find:replace values.
reps = {
    # 'sub': 'dub'
    # Fix periods/commas/semicolons so they don't start a new line after centered math
    re.compile(r'(\n?)\$\$\.'): '.\\1$$',
    re.compile(r'(\n?)\$\$,'): ',\\1$$',
    re.compile(r'(\n?)\$\$:'): ':\\1$$',
    # Fixing spacing issues pandoc creates with concurrent lines of centered math
    re.compile(r'\$\$\n\$\$'): '$$\n\n$$',
    # Add newlines to prevent breaking of KaTeX
    re.compile(r'(\$\$.+?\$\$) ?(.+?)'): '\\1\n\n\\2',
    # Preventing image locations from being lost in conversion
    re.compile(r'\\includegraphicsdata\{.*\}'): replace_img,
    # Removing minipages as the text in them gets thrown away
    #re.compile(r'\\begin\{minipage\}\{.*\}'): '',
    #r'\end{minipage}': '',
    r'\scriptsize': 'figuretext: '
}

f = open(sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

# Doing the actual replacing
newdata = replace_all(filedata, reps)
newdata = process_fboxes(newdata)

# Saving the finished product
f = open(sys.argv[2], 'w', encoding='utf8')
f.write(''.join(newdata))
f.close()
