from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import os
import math
import datetime
import calendar

max_size_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

class DayWriter:


    def __add_rectangle_background_text(self, x, y, size_w, size_h):
        rectangle_offset = 1
        self.rectangle = ImageDraw.Image.new("RGBA", (size_w, size_h + (2 * rectangle_offset)), (255, 255, 255, 128))
        #xy = [(x, y), (x + size_x, y + size_y)]

        self.image.paste(self.rectangle, (x, y-rectangle_offset), mask=self.rectangle)

        #self.draw.rectangle(xy, fill=(255,255,255,10), outline=None)


    def __add_day(self, text, date, x, y):
        date_str = date.strftime("%d.%m.%Y")
        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 20)
        dummy_w, self.rectangle_h = myFont.getsize(max_size_string)
        title_w, title_h = myFont.getsize(text)
        #self.__add_rectangle_background_text(x, y, 50, self.rectangle_h)
        self.draw.text((x, y), text+" "+date_str, font=myFont, fill=(255, 0, 0))
        #self.__add_line_under_obj_h(x, y+title_h)

        return title_w, title_h


    def __print_day(self, text, date, offset_x, offset_y):
        title_size_x, title_size_y = self.__add_day(text, date, offset_x, offset_y)

        return title_size_x, title_size_y


    def __init__(self, text_title, date, game_list, size_h, size_w):
        self.image = Image.new("RGBA", (size_w, size_h), (255, 255, 255, 200))
        self.draw = ImageDraw.Draw(self.image)

        self.__print_day(text_title, date, 0, 0)



if __name__ == "__main__":
    datetime_object = datetime.datetime.now()
    list = [1, 2, 3]

    day_writer = DayWriter("Lundi", datetime_object, list, 200, 200)
    day_writer.image.show()









