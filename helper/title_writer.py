from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import os


class TitleWriter:

    BASE_POSITION_X = 10
    BASE_POSITION_Y = 10

    def __print_title(self):
        img = Image.open(self.base_path)
        d1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 80)
        self.title_w, self.title_h = myFont.getsize("Swiss Tchoukball")
        d1.text((self.BASE_POSITION_X, self.BASE_POSITION_Y), "Swiss Tchoukball", font=myFont, fill=(255, 0, 0))
        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 40)
        self.subtitle_w, self.subtitle_h = myFont.getsize("Matchs de la semaine")
        d1.text((self.title_w - self.subtitle_w, self.BASE_POSITION_Y+self.title_h), "Matchs de la semaine", font=myFont, fill=(0, 0, 0))

        img.show()
        self.new_path = os.path.splitext(self.base_path)[0] + "_withTitle" + ".jpg"
        img.save(self.new_path)

    def __init__(self, path):
        self.base_path = path
        self.__print_title()


