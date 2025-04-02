import calendar

n = int(input("Enter the year: "))
print("\n*******CALENDAR*******")
cal = calendar.TextCalendar(calendar.SUNDAY)  # Create a calendar with Sunday as the first day of the week

for i in range(1,13):
    cal.prmonth(n, i)  # Print each month of the specified year
