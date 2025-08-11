import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
nextweek = today + datetime.timedelta(weeks=1)

print(today)            # 2021-10-19 07:01:22.669886
print(yesterday)        # 2021-10-18 07:01:22.669886
print(tomorrow)         # 2021-10-20 07:01:22.669886
print(nextweek)         # 2021-10-26 07:01:22.669886