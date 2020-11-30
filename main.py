import argparse
import sys
import os

def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description='Description of your app.' )
    parser.add_argument('schedule', help='Path to the csv with the schedule or result')  # describe format
    parser.add_argument('type', help='type of image S for schedule, R for result, Ra for ranking')
    parser.add_argument('-bg', '--background', default="", help='Path to the base image, else, take image from script folder.')

    return parser

def main():
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.backgroun):
        print("File exist")



if __name__ == "__main__":
    main()