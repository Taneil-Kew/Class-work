import calendar
cal = calendar.TextCalendar(6)      # Create an instance
#cal.pryear(2012)                   # What happens here?

#c
cal.prmonth(2018,10)

d = calendar.LocaleTextCalendar(6, "CHINESE")
d.pryear(2012)

print(calendar.isleap(-2664))
#E