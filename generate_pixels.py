from PIL import Image
import os, sys


def gen_pixel_data(list_of_colors, list_of_pixels):
    list_of_colors = list(list_of_colors)
    for i in range(10):
        for i in list_of_colors:
            if i == "1":
                color = (20, 20, 20)
            else:
                color = (255, 255, 255)
            
            for j in range(10):
                list_of_pixels.append(color)


directory = sys.argv[1] + "\\"

if os.path.exists(directory) is False:
    print("No read pixels from image exists.\nPlease read pixels from image first.")
    sys.exit()


with open(f"{directory}full.txt", "r") as f:
    list_of_colors_full = f.read().split("\n")

list_of_pixels = []
for i in list_of_colors_full:
    gen_pixel_data(i, list_of_pixels)

with open(f"{directory}middle.txt", "r") as f:
    list_of_colors_middle = f.read().split("\n")

list_of_pixels_middle = []
for i in list_of_colors_middle:
    gen_pixel_data(i, list_of_pixels_middle)


full = Image.new('RGB', (710, 710))
full.putdata(list_of_pixels)
full.save(f'{directory}full.png')

middle = Image.new('RGB', (310, 310))
middle.putdata(list_of_pixels_middle)
middle.save(f'{directory}middle.png')


