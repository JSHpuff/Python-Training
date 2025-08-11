import datetime

thisTime = datetime.time(14, 0, 0, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

print(thisTime)                         # 14:00:00.000001+08:00
print(thisTime.isoformat())             # 14:00:00.000001+08:00
print(thisTime.tzname())                # UTC+08:00
print(thisTime.strftime('%H:%M:%S'))    # 14:00:00

today = datetime.date.today()
newTime = today.replace(hour=20)

print(newTime)  # 20:00:00.000001+08:00