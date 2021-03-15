from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

from helper.day_writer import DayWriter

import os
import math
import datetime
import calendar


week_day_name_fr = {'Monday' : "Lundi", 'Tuesday' : "Mardi", 'Wednesday' : "Mercredi", 'Thursday' : "Jeudi",
                 'Friday' : "Vendredi", 'Saturday' : "Samedi", 'Sunday' : "Dimanche"}

week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

max_size_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

class GameWriter:

    BASE_POSITION_X_1 = 50
    BASE_POSITION_Y_1 = 150

    BASE_POSITION_X_2 = 580
    BASE_POSITION_Y_2 = 150

    BASE_DAY_HEIGHT = 100
    BASE_DAY_WIDTH  = 500

    BASE_POSITIONS = [(50, 150), (50, 280), (50, 410), (50, 540), (580, 150), (580, 355), (580, 540)]

    LINE_LENGTH = 450
    SPACE_BTW = 80

    def __create_list_date(self, date_of_week):
        theday = date_of_week
        weekday = theday.isoweekday()-1 # -1 to start week on Monday
        # The start of the week
        start = theday - datetime.timedelta(days=weekday)
        # build a simple range
        dates = [start + datetime.timedelta(days=d) for d in range(7)]

        return dates

    def __add_line_under_obj_h(self, x, y):

        line_width = 3
        offset_line = math.ceil(line_width / 2)
        shape =[(x, y+offset_line), (x+self.LINE_LENGTH, y+offset_line)]
        self.draw.line(shape, fill="white", width=line_width)

    def __add_rectangle_background_text(self, x, y, size_w, size_h):
        rectangle_offset = 1
        self.rectangle = ImageDraw.Image.new("RGBA",(size_w,size_h + (2* rectangle_offset)), (255,255,255,128))
        #xy = [(x, y), (x + size_x, y + size_y)]

        self.image.paste(self.rectangle, (x,y-rectangle_offset), mask=self.rectangle)

        #self.draw.rectangle(xy, fill=(255,255,255,10), outline=None)


    def __add_day(self, text, date, x, y):
        date_str = date.strftime("%d.%m.%Y")
        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 20)
        dummy_w, self.rectangle_h = myFont.getsize(max_size_string)
        title_w, title_h = myFont.getsize(text)
        self.__add_rectangle_background_text(x,y, 450, self.rectangle_h)
        self.draw.text((x, y), text+" "+date_str, font=myFont, fill=(255, 0, 0))
        #self.__add_line_under_obj_h(x, y+title_h)

        return title_w, title_h


    def __print_day(self, text, date, offset_x, offset_y):
        self.img_w, self.img_h = self.image.size
        self.draw = ImageDraw.Draw(self.image)
        title_size_x, title_size_y = self.__add_day(text, date, offset_x , offset_y)

        return title_size_x, title_size_y


    def __init__(self, img, game_list, nb_days):
        self.game_list = game_list
        self.image = img.copy()
        self.week_number = game_list.pop(0)
        self.week_list = self.__create_list_date(game_list[0][0])

        if nb_days == 1:
            print("1")
        elif nb_days == 2:
            print("2")
        elif nb_days == 3:
            print("3")
        elif nb_days == 4:
            print("4")
        elif nb_days == 5:
            print("5")
        elif nb_days == 6:
            print("6")
        elif nb_days == 7:
            #easiest way, to show days without any games
            for idx, day in enumerate(week_day):
                width = self.BASE_DAY_WIDTH
                height = self.BASE_DAY_HEIGHT

                self.image_day = DayWriter(week_day_name_fr[day], self.week_list[idx], game_list , height, width)
                self.image.paste(self.image_day.image, self.BASE_POSITIONS[idx], mask=self.image_day.image)

                #self.__print_day(week_day_name_fr[day], self.week_list[idx], self.BASE_POSITIONS[idx][0], self.BASE_POSITIONS[idx][1])
        else:
            print("else")


        self.image.show()

        #save copy of image here
        self.new_path = "Ressources/"+"Week"+"_"+str(self.week_number)+".jpg"

        if self.image.mode in ("RGBA", "P"):
            self.image = self.image.convert("RGB")

        self.image.save(self.new_path, quality=100, subsampling=0)

        self.image.close()
        #self.image.close()


