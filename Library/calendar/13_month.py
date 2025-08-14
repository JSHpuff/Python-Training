# calendar.month(year, month, w=0, l=0) 可以回傳一個格式化的月份字串，
# 效果和 formatmonth 相同。
import calendar

calendar.setfirstweekday(6) # 設定第一天是星期天
print(calendar.month(2021, 10))
'''
    October 2021
Su Mo Tu We Th Fr Sa
                 1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
'''
