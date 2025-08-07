import statistics

# median_grouped() 可以計算數據分組 ( 同樣數值的分成同一組 ) 的中位數。

arr = [1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 5]   # 數據中有重複的數值
a = statistics.median_grouped(arr)    # 計算分組的中位數
print(a)   # 3.8333333333333335