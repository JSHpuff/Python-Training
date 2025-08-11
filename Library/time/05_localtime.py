import time

t = time.time()

# time.localtime(t) 和 time.gmtime(t) 能將 time.time() 得到的時間
# 轉換為 struct_time 格式的本地時間 ( 差別在於 time.gmtime(t) 是回傳 UTC 時間 )。
print(time.localtime(t))
# time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=8, tm_min=8, tm_sec=28, tm_wday=1, tm_yday=292, tm_isdst=0)