"""
Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in as a string format yyyy-mm-dd.
"""

months = ["jan", "feb","mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]
days_31 = [1, 3, 5, 7, 8, 10, 12]
days_28 = 2
days_30 = [4, 6, 9, 11]

def next_day(s):
    ymd = s.split("-")
    date = list(map(int, ymd))
    if date[1] == 12 and date[2] == 31:
        date[0] += 1
        date[1] = 1
        date[2] = 1
        return date
    if date[1] == days_28 and 1 <= date[2] < 28:
        date[2] += 1
    elif date[1] == days_28 and date[2] == 28:
        date[1] += 1
        date[2] = 1
        return date

    if date[1] in days_30 and 1 <= date[2] < 30:
        date[2] += 1
    elif date[1] in days_30 and date[2] == 30:
        date[1] += 1
        date[2] = 1
        return date
    if date[1] in days_31 and 1 <= date[2] < 31:
        date[2] += 1

    elif date[1] in days_31 and date[2] == 31:
        date[1] += 1
        date[2] = 1
    return date

def _print_date(date):
    x = next_day(date)
    return "{}-{:02}-{:02}".format(x[0], x[1], x[2])


