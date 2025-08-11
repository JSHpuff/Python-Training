# time.mktime(t) 可以將 struct_time 格式的時間轉換回秒數。
import time

t = time.time()
t1 = time.localtime(t)
t2 = time.mktime(t1)

print(t)    # 1634631418.445556
print(t1)   # time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=8, tm_min=16, tm_sec=58, tm_wday=1, tm_yday=292, tm_isdst=0)
print(t2)   # 1634631418.0