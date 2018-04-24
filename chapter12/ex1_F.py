import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)                   # What happens here? prints a calandar for 2012

#B
cal = calendar.TextCalendar(1)
cal.pryear(2018)

#C
cal = calendar.TextCalendar()
cal.prmonth(2018,10)

#D
d = calendar.LocaleTextCalendar(6, "CHINESE")
d.pryear(1)

#E
print(calendar.isleap(-63))
# it expects a year
#true or false
#a boolean function


