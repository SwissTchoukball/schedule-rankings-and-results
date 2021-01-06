import csv

class WeekExtracter:

    WEEK_NUMBER = 53

    def __created_empty_wk_list(self):
        self.week_list = [[] for x in range(self.WEEK_NUMBER)]

        for i, elem in enumerate(self.week_list):
            elem.append(i+1)


    def __init__(self, list):
        self.base_list = sorted(list)
        self.__created_empty_wk_list()


    def get_list_parsed(self):
        my_week_list = []
        my_list = []

        for elem in self.base_list:
            week_number = elem[0].isocalendar()[1]
            self.week_list[week_number].append(elem)

        return self.week_list



if __name__ == "__main__":
    print("WeekExtracter")