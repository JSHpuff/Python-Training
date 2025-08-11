# time.asctime(t) 可以將 struct_time 格式的時間轉換為文字顯示。

import time

t = time.time()
t1 = time.localtime(t)
t2 = time.asctime(t1)

print(t)    # 1634631577.3905456
print(t1)   # time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=8, tm_min=19, tm_sec=37, tm_wday=1, tm_yday=292, tm_isdst=0)
print(t2)   # Tue Oct 19 08:19:37 2021