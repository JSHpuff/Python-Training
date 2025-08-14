import calendar

tc = calendar.TextCalendar()
tc.setfirstweekday(4)   # 設定星期五為第一天
tc.prmonth(2021, 10)

'''
    October 2021
Fr Sa Su Mo Tu We Th
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
'''