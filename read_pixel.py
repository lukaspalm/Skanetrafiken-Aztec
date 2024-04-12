from PIL import Image
import math
import sys
import os

def get_pixel_color(image, x, y):
    pixel_color = image.getpixel((x, y))
    return pixel_color

def compare(rgb_tuple):
    threshold = (125, 125, 125)
    if all(x < y for x, y in zip(rgb_tuple, threshold)):
        return "1"
    if all(x > y for x, y in zip(rgb_tuple, threshold)):
        return "0"
    else:
        return "?"
def getpixel(square_width, square_height, image, row, col):
    x = math.ceil((col-1)*square_width + (square_width/2))
    y = math.ceil((row-1)*square_width + (square_width/2))
    pixel_color = get_pixel_color(image, x, y)
    return compare(pixel_color)
    

# Example usage

imgpath = sys.argv[1]
jpgpath = imgpath + ".jpg"
pngpath = imgpath + ".png"
directory = str(imgpath).replace("assets", "assets\\..") + "\\"

if os.path.exists(jpgpath):
    image = Image.open(jpgpath)
    path = ".jpg"
    with open(jpgpath, "rb") as f:
        imgsrc = f.read()

elif os.path.exists(pngpath):
    image = Image.open(pngpath)
    path = ".png"
    with open(pngpath, "rb") as f:
        imgsrc = f.read()
else:
    print("No image found.")
    sys.exit()

if os.path.exists(directory) is False:
    os.makedirs(directory)

with open(f"{directory}original{path}", "wb") as f:
    f.write(imgsrc)
    f.close


    

square_height = image.size[1]/71
square_width = image.size[0]/71
row = 41
col = 41

with open(f"{directory}full.txt", "w") as f:
    pixel_list = []
    for i in range(1, 72):
        string = ""
        for j in range(1, 72):
            string += getpixel(square_width, square_height, image, i, j)
        pixel_list.append(string)
    for i in pixel_list:
        print(i, file=f)
with open(f"{directory}middle.txt", "w") as f:
    pixel_list = []
    for i in range(21, (21+31)):
        string = ""
        for j in range(21, (21+31)):
            string += getpixel(square_width, square_height, image, i, j)
        pixel_list.append(string)
    for i in pixel_list:
        print(i, file=f)



