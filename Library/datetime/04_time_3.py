import datetime

thisTime = datetime.time(14, 0, 0, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

print(thisTime)
print(thisTime.isoformat())
print(thisTime.tzname())
print(thisTime.strftime('%H:%M:%S'))

today = datetime.date.today()
newTime = today.replace(hour=20)

print(newTime)