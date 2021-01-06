import argparse
import sys
import os
from helper.csv_parser import CSVParser
from helper.extract_by_week import WeekExtracter
from helper.background_resizer import BKResizer
from helper.title_writer import TitleWriter
from helper.game_writer import GameWriter

import datetime

def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description='Description of your app.' )
    parser.add_argument('csv', help='Path to the csv with the schedule or result')  # describe format
    parser.add_argument('type', help='type of image S for schedule, R for result, Ra for ranking')
    parser.add_argument('-bg', '--background', default="", help='Path to the base image, else, take image from script folder.')

    return parser

def main():
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.isfile(parsed_args.background):
        print("Background exist")
    if os.path.isfile(parsed_args.csv):
        print("csv exist")


if __name__ == "__main__":
    main()
    my_csv = CSVParser("Ressources/schedule.csv")
    my_image = BKResizer("Ressources/background.jpg")
    my_week_list = WeekExtracter(my_csv.get_list())
    background = my_image.image
    background_title = TitleWriter(background)
    for elem in my_week_list.get_list_parsed():
        if len(elem) > 1:
            my_game_writer = GameWriter(background_title.image, elem, 7)

    #Last line to close the image
    my_image.image.close()


