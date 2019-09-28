from PIL import Image
import json


def image_converter(shapes):
    with open("pixels.json", "w") as pixelFile:
        #Dict for storing all pixel values
        image_pixels = {"images": [], "answer_key": []}
        for i in range(1, 101):
            image_colors = []
            im = Image.open(f'squares/drawing({i}).png')
            pix = im.load()
            print(im.size)
            for x in range(im.size[0]):
                for y in range(im.size[1]):
                    image_colors.append(pix[x+1, y+1])
            image_pixels["images"].append(image_colors)
        pixelFile.write(json.load(image_pixels))