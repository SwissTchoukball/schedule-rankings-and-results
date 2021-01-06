import csv
from datetime import datetime
from datetime import time

class CSVParser:

    def __init__(self, path):
        self.path = path


    def get_list(self):
        my_csv_list = []

        with open(self.path, newline='') as file:
            reader = csv.reader(file, delimiter=',')
            my_csv_list = list(reader)
            for elem in my_csv_list:
                print(elem)
                elem[0] = datetime.strptime(elem[0] + ' ' + elem[1], '%d.%m.%Y %Hh%M')

        return my_csv_list


if __name__ == "__main__":
    my_csv = CSVParser("../Ressources/schedule.csv")
    print(my_csv.get_list())

