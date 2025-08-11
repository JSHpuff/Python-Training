import datetime

thisTime = datetime.time(14, 0, 0, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

print(thisTime) # 14:00:00.000001+08:00