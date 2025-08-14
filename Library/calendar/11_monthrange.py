# calendar.monthrange(year, month) 
# 可以回傳某年某月的第一天是星期幾 ( 星期一為 0 )，以及這個月的天數。
import calendar

print(calendar.monthrange(2021, 10))
# (4, 31)  2021 的 10 月有 31 天，10 月第一天是星期五

print(calendar.monthrange(2021, 11))
# (0, 30)  2021 的 11 月有 30 天，11 月第一天是星期一