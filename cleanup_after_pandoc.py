#!/usr/bin/python
import re
import sys
import os

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

def image_key(name):
    return tuple(int(num) for num in name.split('_', 2)[:2])

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
        if name not in self.image_dict:
            self.image_dict[name] = Image()
            self._set_image_order()
        self.image_dict[name].add(**{ext[1:]: filename})

    def get(self, index):
        return self.image_dict[self.image_order[index]]

image_index = ImageIndex()

for filename in os.listdir(IMAGE_DIR):
    image_index.add(filename)

def replace_img(prefer_png=False):
    def do_replace(match):
        num = int(match.group(1))

        image = image_index.get(num-1)

        if image.R and not prefer_png:
            with open(os.path.join(IMAGE_DIR, image.R), 'r') as file:
                code = file.read()
                return "```{r}\n%s\n```" % code
        elif image.png:
            return "[Fig. %d](images/%s)" % (num, image.png)
        else:
            return "[IMAGE MISSING]"
    return do_replace

# Replace method
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text

block_headers = {
    'defn': "**Definition**:  ",
    'xmpl': "**Example**:  ",
    'notes': "**Note**:  "
}

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
            else:
                block_stack.pop()
        else:
            resultlines.append('> ' * len(block_stack) + line)
    return '\n'.join(resultlines)


# Dictionaries with our find:replace values.
image_regex = re.compile(r'::: picture\n(\d+)\n:::')
rep_sets = [{
    image_regex: replace_img(False)
},
{
    image_regex: replace_img(True)
}]


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
