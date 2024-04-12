from PIL import Image

def gen_letter_pixels(letter):
    letter_bin = format(ord(letter), '08b')
    



def gen_pixel_data(list_of_colors):
    global list_of_pixels
    list_of_colors = list(list_of_colors)
    for i in range(10):
        for i in list_of_colors:
            if i == "1":
                color = (20, 20, 20)
            else:
                color = (255, 255, 255)
            
            for j in range(10):
                list_of_pixels.append(color)

gen_letter_pixels("2")

