import math
import time

import PIL
import numpy as np
from PIL import Image

pixels = []


def get_div(i):
    return math.ceil(math.sqrt(i))


f = open("new.jpg", "r", encoding='utf-8')

pan_tadeusz = f.read()

x_range = get_div(len(pan_tadeusz) / 3)
y_range = get_div(len(pan_tadeusz) / 3)
print(x_range)
print(y_range)

pixels_x = []
index = 0
mode = 0

for x in range(x_range):
    for y in range(y_range):
        if index + 2 >= len(pan_tadeusz):
            mode = 1
            pixels_x.append((0, 0, 0))
        else:
            # print(ord(pan_tadeusz[index]), ord(pan_tadeusz[index + 1]), ord(pan_tadeusz[index + 2]))

            pixels_x.append((ord(pan_tadeusz[index]), ord(pan_tadeusz[index + 1]), ord(pan_tadeusz[index + 2])))
        index += 3
    pixels.append(pixels_x)

    pixels_x = []
    if mode == 1:
        break

array = np.array(pixels, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save('new.bmp')