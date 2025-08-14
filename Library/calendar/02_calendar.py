import calendar

c = calendar.Calendar()

print(list(c.iterweekdays()))
# [0, 1, 2, 3, 4, 5, 6]

print(list(c.itermonthdates(2021, 10)))
# [datetime.date(2021, 9, 27), datetime.date(2021, 9, 28)]

print(list(c.itermonthdays(2021, 10)))
# [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

print(list(c.itermonthdays2(2021, 10)))
# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 5).....

print(c.monthdatescalendar(2021, 10))
# [[datetime.date(2021, 9, 27), datetime.date(2021, 9, 28).....

print(c.monthdayscalendar(2021, 10))
# [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10]......

print(c.monthdays2calendar(2021, 10))
# [[(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 5).....

print(c.yeardatescalendar(2021))
# [[[[datetime.date(2020, 12, 28), datetime.date(2020, 12, 29)....

print(c.yeardayscalendar(2021))
# [[[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10]....

print(c.yeardays2calendar(2021))
# [[[[(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 5)....