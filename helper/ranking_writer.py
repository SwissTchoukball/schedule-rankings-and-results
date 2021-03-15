from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

from helper.day_writer import DayWriter

import os
import math
import datetime
import calendar


max_size_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

class RankWriter:

    BASE_POSITION_X_1 = 150  #largeur
    BASE_POSITION_Y_1 = 150 #hauter

    BASE_POSITION_X_2 = 580
    BASE_POSITION_Y_2 = 150

    ROW_HEIGHT = 50
    POS_WIDTH = 50
    TEAM_WIDTH = 400
    PLAYED_WIDHT = 50
    POINT_WIDTH = 50

    BASE_POSITIONS = [(50, 150), (50, 280), (50, 410), (50, 540), (580, 150), (580, 355), (580, 540)]

    LINE_LENGTH = 450
    SPACE_BTW = 1


    def __add_rectangle_background_text(self, x, y, size_w, size_h):
        rectangle_offset = 0
        self.rectangle = ImageDraw.Image.new("RGBA",(size_w,size_h), (255,255,255,128))
        #xy = [(x, y), (x + size_x, y + size_y)]

        self.image.paste(self.rectangle, (x,y), mask=self.rectangle)

        #self.draw.rectangle(xy, fill=(255,255,255,10), outline=None)


    def __add_row(self, list, position):
        print(list)
        #self.__add_rectangle_background_text(self.BASE_POSITION_X_1, self.BASE_POSITION_Y_1, self.POS_WIDTH, self.ROW_HEIGHT)
        #Print pos rectangle
        self.__add_rectangle_background_text(self.BASE_POSITION_X_1, self.BASE_POSITION_Y_1+(position*(self.ROW_HEIGHT+self.SPACE_BTW)), self.POS_WIDTH, self.ROW_HEIGHT)
        #print team pos
        self.__add_rectangle_background_text(self.BASE_POSITION_X_1+self.POS_WIDTH, self.BASE_POSITION_Y_1+(position*(self.ROW_HEIGHT+self.SPACE_BTW)), self.TEAM_WIDTH, self.ROW_HEIGHT)
        #print played width
        self.__add_rectangle_background_text(self.BASE_POSITION_X_1+self.POS_WIDTH+self.TEAM_WIDTH, self.BASE_POSITION_Y_1+(position*(self.ROW_HEIGHT+self.SPACE_BTW)), self.PLAYED_WIDHT, self.ROW_HEIGHT)

    def __init__(self, img, rank_list):
        self.rank_list = rank_list
        self.image = img.copy()

        for elem in self.rank_list:
            self.__add_row(elem, int(elem[0]))


        self.image.show()


        #save copy of image here
        self.new_path = "Ressources/"+"Ranking"+".jpg"

        if self.image.mode in ("RGBA", "P"):
            self.image = self.image.convert("RGB")

        self.image.save(self.new_path, quality=100, subsampling=0)

        self.image.close()
        #self.image.close()


