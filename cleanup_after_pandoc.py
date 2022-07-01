#!/usr/bin/python
import re
import sys
import os

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

# Sort key for images, so that (11_1 doesn't sort before 2_1).
def image_key(name):
    return tuple(int(num) for num in name.split('_', 2)[:2])

# Simple class to bundle together files representing the same image.
class Image(object):
    png = None
    R = None

    def __init__(self, png=None, R=None):
        self.add(png, R)

    def add(self, png=None, R=None):
        if png:
            self.png = png
        if R:
            self.R = R

# An index serving two purposes:
# - easily ensure filenames get bundled together into Image objects appropriately
#   (we want 1_1_blah.png and 1_1_blah.R to be bundled together)
# - allow retrieving an image by index, which represents the order in which the
#   images should appear in the file
class ImageIndex(object):
    image_dict = None
    image_order = None

    def __init__(self):
        self.image_dict = {}
        self.image_order = []

    def _set_image_order(self):
        self.image_order = sorted(self.image_dict.keys(), key=image_key)

    def add(self, filename):
        name, ext = os.path.splitext(filename)
        # If the name is not in the index, create a new Image object for it;
        # otherwise, add this file to the existing Image object for this name
        if name not in self.image_dict:
            self.image_dict[name] = Image()
            self._set_image_order()
        self.image_dict[name].add(**{ext[1:]: filename})

    def get(self, index):
        return self.image_dict[self.image_order[index]]

image_index = ImageIndex()

for filename in os.listdir(IMAGE_DIR):
    image_index.add(filename)

# Higher-order function returning a replace function for images.
# If prefer_png is True, then we will ignore .R versions of images and simply
# insert references to the PNG images into the Markdown.
# If prefer_png is False, we will insert the .R file as a ```{r}``` code block
# if one is available, or otherwise a reference to the PNG.
# (Hopefully later we will have a Markdown parser that understands the R blocks.)
def replace_img(prefer_png=False):
    def do_replace(match):
        num = int(match.group(1))

        image = image_index.get(num-1)

        if image.R and not prefer_png:
            with open(os.path.join(IMAGE_DIR, image.R), 'r') as file:
                code = file.read()
                return "```{r}\n%s\n```" % code
        elif image.png:
            return "![Fig. %d](images/%s)" % (num, image.png)
        else:
            return "[IMAGE MISSING]"
    return do_replace

dollar_counter = 0
def replace_dollars(match):
    global dollar_counter
    dollar_counter += 1
    if dollar_counter % 2 == 1:
        return '\n\n$$' + match.group(2)
    else:
        return match.group(1) + '$$\n\n'

# Replace method
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text

# Headers we want to show at the top of on different kinds of blocks.
block_headers = {
    'defn': "**Definition**:  ",
    'xmpl': "**Example**:  ",
    'notes': "**Note**:  "
}

# Process possibly-nested ::: (blockname) ::: blocks.
# We want to quote-indent them with >, with correct nesting, and add headers
# where defined in block_headers.
def process_blocks(text):
    block_regex = re.compile(r':::(?: (\w+))?')
    block_stack = []
    resultlines = []
    for line in text.splitlines():
        match = block_regex.match(line)
        if match:
            if match.group(1):
                # Starting a new block
                block_stack.append(match.group(1))
                if match.group(1) in block_headers:
                    resultlines.append('> ' * len(block_stack) + block_headers[match.group(1)])
                    resultlines.append('> ' * len(block_stack))
            else:
                # Ending a block
                block_stack.pop()
        else:
            # Just insert the line with the correct level of blockquote nesting
            resultlines.append('> ' * len(block_stack) + line)
    return '\n'.join(resultlines)


# Dictionaries with our find:replace values.
# The script will output one file for each of the rep_sets, created by running
# that set of replacements and then processing blocks.
# (It needs that many output filenames as command line arguments!)
# Right now, we want one output file with all PNG images and one with R blocks.
image_regex = re.compile(r'::: picture\n(\d+)\n:::')
rep_sets = [{
    image_regex: replace_img(False),
    # Remove redundant backslashes
    re.compile(r'\\\n\$\$'): '\n$$',
    # Cleaning up one particular example
    re.compile(r'\\####'): '####',
    # Add newlines to prevent breaking of KaTeX or other LaTeX interpretors
    re.compile(r'(\n{0,2})\$\$(\n{0,2})'): replace_dollars,
    # Adds spaces to try to fix a LaTeX rendering bug (BREAKS MORE THAN IT FIXES CURRENTLY)
    #re.compile(r'([^\$\\])\$([^\$])'): '\\1 $\\2',
    # Workaround for a LaTeX rendering bug (Adds spaces that aren't swallowed by Pandoc
    'BIL': ' ',
    'NIL': '',
    'Ö': ' ',
},
{
    image_regex: replace_img(True),
    # Remove redundant backslashes
    re.compile(r'\\\n\$\$'): '\n$$',
    # Cleaning up one particular example
    re.compile(r'\\####'): '####',
    # Add newlines to prevent breaking of KaTeX or other LaTeX interpretors
    re.compile(r'(\n{0,2})\$\$(\n{0,2})'): replace_dollars,
    # Adds spaces to try to fix a LaTeX rendering bug (BREAKS MORE THAN IT FIXES CURRENTLY)
    re.compile(r'([^\$\\])\$([^\$\n]+?)\$([^\$])'): '\\1 $\\2 $\n\\3',
    # Workaround for a LaTeX rendering bug (Adds e.g. spaces that aren't swallowed by Pandoc)
    'BIL': ' ',
    'NIL': '',
    'Ö': ' ',
}
]


f = open(sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

# Doing the actual replacing
for i, rep in enumerate(rep_sets):
    newdata = replace_all(filedata, rep_sets[i])
    newdata = process_blocks(newdata)

    # Saving the finished product
    f = open(sys.argv[2+i], 'w', encoding='utf8')
    f.write(''.join(newdata))
    f.close()
