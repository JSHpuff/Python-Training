# Mutable → 內容可以直接改變，不用創建新物件。
# Immutable → 內容不能改變，任何“修改”都是創建新物件。

# Immutable
counter = 100
print(id(counter))
print(hex(id(100)))

counter = 200
print(counter)
print(hex(id(counter)))

# Mutable
ratings = [1, 2, 3]
print(hex(id(ratings)))

ratings.append(4)
print(ratings)
print(hex(id(ratings)))