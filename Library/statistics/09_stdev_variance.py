# stdev() 和 variance() 可以計算數據的樣本標準差和變異數。

import statistics

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = statistics.stdev(arr)
b = statistics.variance(arr)

print(a)
print(b)