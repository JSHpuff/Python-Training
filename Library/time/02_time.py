import time

# time.time() 執行後會回傳 1970 年 1 月 1 日 00:00:00 到現在的秒數 
# ( 精確度到 1/1000000 秒 )，
# 秒數使用浮點數 float 的格式，如果改成 time.time_ns() 會回傳 ns 數 
# ( 1/1000000000 秒 )
print(time.time())      # 1634629287.537577
print(time.time_ns())   # 1634629287537744648