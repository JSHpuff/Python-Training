# calendar.weekheader(n) 可以回傳星期幾的開頭縮寫，n 的範圍是 1～3。
import calendar

print(calendar.weekheader(1)) # M T W T F S S
print(calendar.weekheader(2)) # Mo Tu We Th Fr Sa Su
print(calendar.weekheader(3)) # Mon Tue Wed Thu Fri Sat Sun