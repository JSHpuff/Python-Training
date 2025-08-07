# pstdev() 和 pvariance() 可以計算數據的母體標準差和變異數。

import statistics

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = statistics.pstdev(arr)
b = statistics.pvariance(arr)

print(a)
print(b)