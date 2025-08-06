import calendar

year = int(input("Enter Year: "))
mon = int(input("Enter Month: "))

cal = calendar.month(year, mon)
print(cal)
