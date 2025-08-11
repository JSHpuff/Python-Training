# time.localtime(t) 和 time.gmtime(t) 能將 time.time() 得到的時間，
# 轉換為 struct_time 格式的本地時間 ( 差別在於 time.gmtime(t) 是回傳 UTC 時間 )。

import time

t = time.time()
tt = time.localtime(t)

print(tt.tm_year) # 2021
print(tt.tm_mon) # 10