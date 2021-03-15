import datetime
from datetime import time

week_day_name_fr = {'Monday' : "Lundi", 'Tuesday' : "Mardi", 'Wednesday' : "Mercredi", 'Thursday' : "Jeudi",
                 'Friday' : "Vendredi", 'Saturday' : "Samedi", 'Sunday' : "Dimanche"}

week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class Week:

    def __create_list_date(self, date_of_week):
        theday = date_of_week
        weekday = theday.isoweekday()-1 # -1 to start week on Monday
        # The start of the week
        start = theday - datetime.timedelta(days=weekday)
        # build a simple range
        dates = [start + datetime.timedelta(days=d) for d in range(7)]

        return dates

    def __init__(self, week_number, match_of_week):
        self.wk_nb = week_number
        self.week_game = match_of_week

        if len(match_of_week) > 0 :
            self.days_str = []
            self.days_date = self.__create_list_date(match_of_week[0])
            for idx, day in enumerate(week_day):
                day_str = week_day_name_fr[day] + " " + self.days_date[idx].strftime("%d.%m.%Y")
                self.days_str.append(day_str)
            for game in self.week_game:
                #Add each game in right position in a new list of size 7 represnting each day
        else:
            self.days_date = []
            self.days_str = []


if __name__ == "__main__":
    date = datetime.datetime.now()
    list = []
    list.append(date)
    week = Week(1, list)
    print(week.days_date)
    print(week.days_str)