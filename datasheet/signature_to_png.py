#!/usr/bin/env python3

# Takes signature/date as input, increases contrast, makes it black/white, adds alpha channel by removing white background.
# Usage: ./signature_to_png.py raw_file.png output.png threshold

# Example: ./signature_to_png.py fake_signature_in.png fake_signature.png 150

import sys

from PIL import Image
import numpy as np


assert len(sys.argv) == 4

# settings
raw_file=sys.argv[1]
threshold=int(sys.argv[3])
white = (255, 255, 255, 255)
black = (0,0,0,255)
gray = (127, 127, 127, 127)
yellow = (0, 255, 0, 255)

# open --> grayscale
img = Image.open(raw_file).convert('L')
img_arr = np.array(img)

# grayscale --> rgba
img_arr[img_arr<threshold]=0
img_arr[img_arr>=threshold]=1
img = Image.fromarray(img_arr*255).convert('RGBA')

# transparenting white pixel and coloring active pixel
newData = []
datas = img.getdata()
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(black)


img.putdata(newData)
img.save(sys.argv[2], "PNG")
