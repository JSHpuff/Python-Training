import datetime

now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))

print(now)                                  # 2021-10-19 14:25:46.962975+08:00
print(now.date())                           # 2021-10-19
print(now.time())                           # 14:25:46.962975
print(now.tzname())                         # UTC+08:00
print(now.weekday())                        # 1
print(now.isoweekday())                     # 2
print(now.isocalendar())                    # (2021, 42, 2)
print(now.isoformat())                      # 2021-10-19 14:25:46.962975+08:00
print(now.ctime())                          # Tue Oct 19 14:48:38 2021
print(now.strftime('%Y/%m/%d %H:%M:%S'))    # 2021/10/19 14:48:38
print(now.timetuple())
# time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=16, tm_min=8, tm_sec=6, tm_wday=1, tm_yday=292, tm_isdst=-1)