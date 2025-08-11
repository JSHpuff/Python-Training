import datetime

today = datetime.date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
print(today.isocalendar())
print(today.isoformat())
print(today.ctime())
print(today.strftime('%Y.%m.%d'))

newDay = today.replace(year=2020)
print(newDay)