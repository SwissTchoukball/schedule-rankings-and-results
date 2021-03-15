import csv

class WeekExtracter:

    WEEK_NUMBER = 53
    WEEK_LIST = [[],[],[],[],[],[],[]]

    def __created_empty_wk_list(self):
        self.week_list = [[] for x in range(self.WEEK_NUMBER)]

        for i, elem in enumerate(self.week_list):
            elem.append(i+1)
            #elem.append(self.WEEK_LIST)

        print(self.week_list)


    def __init__(self, list):
        self.base_list = sorted(list)
        self.__created_empty_wk_list()


    def get_list_parsed(self):
        my_week_list = []
        my_list = []

        for elem in self.base_list:
            week_day = elem[0].weekday()
            print(elem[0].isocalendar()[1])
            week_number = elem[0].isocalendar()[1]
            self.week_list[week_number].append(elem)

        return self.week_list



if __name__ == "__main__":
    print("WeekExtracter")