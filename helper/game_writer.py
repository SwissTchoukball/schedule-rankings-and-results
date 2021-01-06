from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import os
import math
import datetime
import calendar

week_day_name_fr = {'Monday' : "Lundi", 'Tuesday' : "Mardi", 'Wednesday' : "Mercredi", 'Thursday' : "Jeudi",
                 'Friday' : "Vendredi", 'Saturday' : "Samedi", 'Sunday' : "Dimanche"}

week_day = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

class GameWriter:

    BASE_POSITION_X_1 = 50
    BASE_POSITION_Y_1 = 150

    BASE_POSITION_X_2 = 580
    BASE_POSITION_Y_2 = 150

    BASE_POSITIONS = [(50, 150),(50, 280),(50, 410),(50, 540),(580, 150),(580, 355),(580, 540)]

    LINE_LENGTH = 450
    SPACE_BTW = 80


    def __add_line_under_obj_h(self, x, y):

        line_width = 3
        offset_line = math.ceil(line_width / 2)
        shape =[(x, y+offset_line), (x+self.LINE_LENGTH, y+offset_line)]
        self.draw.line(shape, fill="white", width=line_width)


    def __add_day(self, text, x, y):

        myFont = ImageFont.truetype('Ressources/FloraStd-Bold.ttf', 20)
        title_w, title_h = myFont.getsize(text)
        self.draw.text((x, y), text, font=myFont, fill=(255, 0, 0))
        self.__add_line_under_obj_h(x, y+title_h)


        return title_w, title_h

    def __print_day(self, text, offset_x, offset_y):
        self.img_w, self.img_h = self.image.size
        self.draw = ImageDraw.Draw(self.image)

        self.__add_day(text, offset_x , offset_y)


    def __init__(self, img, game_list, nb_days):
        self.game_list = game_list
        self.image = img.copy()
        week_number = game_list.pop(0)

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
                print(idx, day)
                self.__print_day(week_day_name_fr[day], self.BASE_POSITIONS[idx][0], self.BASE_POSITIONS[idx][1])
        else:
            print("else")

        #print(game_list)
        #for idx, elem in enumerate(game_list):
            #    date = elem[0]
            #    day_name_fr = week_day_name_fr[calendar.day_name[date.weekday()]]
            #    date_str = date.strftime("%d.%m.%Y")
        #    self.__print_day(day_name_fr + " " + date_str, idx)


        self.image.show()

        #save copy of image here
        self.new_path = "Ressources/"+"Week"+"_"+str(week_number)+".jpg"
        self.image.save(self.new_path, quality=100, subsampling=0)

        self.image.close()
        #self.image.close()


