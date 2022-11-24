from PIL import Image, ImageDraw
import random

def mirror(arr,even=True):
    n_arr = arr
    f_arr = n_arr[::-1]
    if even:
        for i in f_arr:
            n_arr.append(i)
    else:
        for i in range(1,len(f_arr)):
            n_arr.append(f_arr[i])
    return n_arr

def make_bitmap(size):
    bitmap = []
    for i in range(size[0]):
        row = []
        if size[1]%2==0:
            for j in range(size[1]//2):
                row.append(random.randint(0,1))
            row = mirror(row)
        else:
            for j in range((size[1]//2)+1):
                row.append(random.randint(0,1))
            row = mirror(row,False)
        bitmap.append(row)
    return bitmap

def make_img(arr, size, name):
    scl =  size[0]/max(len(arr),len(arr[1]))
    img = Image.new("1", size)
    draw = ImageDraw.Draw(img)
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 0:
                draw.rectangle([x*scl,y*scl,(x*scl)+scl,(y*scl)+scl],fill = 0)
            if arr[y][x] == 1:
                draw.rectangle([x*scl,y*scl,(x*scl)+scl,(y*scl)+scl],fill = 1)
    img.save(f'Generated_art/{name}.jpg')

make_img(make_bitmap((6,6)),(1000,1000),'jakub')