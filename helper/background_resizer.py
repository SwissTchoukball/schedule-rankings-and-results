from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import os


class BKResizer:

    BASE_WIDTH = 1080


    def __resize_background(self):

        img = Image.open(self.base_path)
        width_percent = (self.BASE_WIDTH / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        self.image = img.resize((self.BASE_WIDTH, height_size), Image.ANTIALIAS)
        self.new_path = os.path.splitext(self.base_path)[0]+"_resized"+".jpg"
        self.image.save(self.new_path)

        image_transparent = Image.new('RGBA', (self.BASE_WIDTH, height_size), (0, 0, 0, 0))
        image_transparent.paste(self.image, (0, 0))
        self.image = image_transparent
        #self.image.close()


    def __init__(self, path):
        self.base_path = path
        self.__resize_background()

