from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import os


class TitleWriter:

    def __print_title(self):
        img = Image.open(self.base_path)
        d1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 80)
        d1.text((10, 10), "Swiss Tchoukball", font=myFont, fill=(255, 0, 0))
        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 40)
        d1.text((10, 60), "Matchs de la semaine", font=myFont, fill=(0, 0, 0))

        img.show()
        self.new_path = os.path.splitext(self.base_path)[0] + "_withTitle" + ".jpg"
        img.save(self.new_path)

    def __init__(self, path):
        self.base_path = path
        self.__print_title()


