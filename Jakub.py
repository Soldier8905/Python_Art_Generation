# imports required packages/modules
from PIL import Image, ImageDraw, ImageFilter
import random

# imports the potentail color schemes that have been made for Jakub to pick from
from color_pallet import color_choices

# sets random color scheme from the list provided in the color_pallet.py file
color_scheme = random.choice(color_choices)

# converts an RGB value to a HEX value in the right format so that PIL can use it
def RGB2HEX(rgb: list) -> str:
    hex_value = '#'
    for i in rgb:
        value = f'{hex(i)[2::]}'
        if len(value) != 2:
            value = f'0{value}'
        hex_value += value
    return hex_value

# flips an arr and add it to the end of the inputed arr
def mirror(arr: list, even=True) -> list:
    n_arr = arr
    f_arr = n_arr[::-1]
    if even:
        for i in f_arr:
            n_arr.append(i)
    else:
        for i in range(1,len(f_arr)):
            n_arr.append(f_arr[i])
    return n_arr

# produces a 2D arr which reprecents the img and what it should look like
# this takes the dimensions of the img as input
def make_img_arr(size: tuple = (10,10)) -> list:
    img_arr = []
    for i in range(size[0]):
        row = []
        if size[1]%2==0:
            for j in range(size[1]//2):
                row.append(random.choice(color_scheme))
            row = mirror(row)
        else:
            for j in range((size[1]//2)+1):
                row.append(random.choice(color_scheme))
            row = mirror(row,False)
        img_arr.append(row)
    return img_arr

# takes the 2D arr which represents the img and turns it into a PIL image object
def make_img(arr: list, scl: int, name: str) -> Image.Image:
    size = (len(arr[0])*scl, len(arr)*scl)
    img = Image.new("RGB", size, '#f1efac')
    draw = ImageDraw.Draw(img)
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            draw.rectangle([x*scl,y*scl,(x*scl)+scl,(y*scl)+scl],fill = RGB2HEX(arr[y][x]))
    return img

# creates and saves img
img = make_img(make_img_arr((20,20)),10,'jakub')
img.save('Generated_art/jakub.jpg')