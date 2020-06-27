import calendar

# calendar month starting from Sunday
c = calendar.TextCalendar(calendar.SUNDAY)
print(c.formatmonth(2022, 1))
print(50 * '-')

# calendar month starting from default Monday
c = calendar.TextCalendar()
print(c.formatmonth(2022, 1))
print(50 * '-')

c = calendar.HTMLCalendar()
print(c.formatmonth(2022, 1))
print(50 * '-')

print("Week days in number starting from Monday with index 0")
weekdays = calendar.TextCalendar().iterweekdays()
for name in weekdays:
    print(name, end = ",")
print()
print(50 * '-')

print("Month days: Starting from Monday with 0 if week starts from other day.")
monthdays = calendar.TextCalendar().itermonthdays(2022, 1)
for name in monthdays:
    print(name, end = ",")
print()
print(50 * '-')

print("Week Days")
days = calendar.day_name
for day in days:
    print(day)
print(50 * '-')

print("Months")
months = calendar.month_name
for month in months:
    print(month)
print(50 * '-')

for month in range(1, 13):
    print(calendar.month_name[month])
    cal = calendar.monthcalendar(2020, month)

    week1 = cal[0]
    for weekday in week1:
        print(weekday)
    print(25 * '-')

