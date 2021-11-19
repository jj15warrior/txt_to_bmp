import time

from PIL import Image

image = Image.open('converted.bmp')
x_s = image.size[1]
y_s = image.size[0]
print(x_s, y_s)
pan_tadeusz = open("output.txt", "w", encoding='utf-8')

for x in range(x_s):
    for y in range(y_s):
        col = image.getpixel((y, x))
        # print(col)
        pan_tadeusz.write(chr(col[0]))
        pan_tadeusz.write(chr(col[1]))
        pan_tadeusz.write(chr(col[2]))