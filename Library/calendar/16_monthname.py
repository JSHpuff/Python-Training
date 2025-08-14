# calendar.month_name、calendar.month_abbr 
# 使用後會回傳 1～12 月的名稱或縮寫 ( 產生後的第一個值會是空值 )。
import calendar

print(list(calendar.month_name))
# ['', 'January', 'February', 'March', 'April', 
# 'May', 'June', 'July', 'August', 'September', 
# 'October', 'November', 'December']