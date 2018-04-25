import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)                   # What happens here?

#1B start on thursday
cal = calendar.TextCalendar(3)      # Create an instance
cal.pryear(2018)                   # What happens here?

#C
cal= calendar.TextCalendar(6)
cal.prmonth(2018,10)

#D
d = calendar.LocaleTextCalendar(6, "esperanto")
d.pryear(2012)

#E
print(calendar.isleap(-1600000))
#it expects a year
#it returns true or false
#boolean

