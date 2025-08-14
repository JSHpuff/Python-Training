import calendar

html = calendar.HTMLCalendar()

print(html.formatyear(2021, width=4))
print(html.formatyearpage(2021, width=4))