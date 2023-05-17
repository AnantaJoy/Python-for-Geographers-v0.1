from datetime import datetime

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)

# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
print(datetime(2019, 10, 21, 16, 29, 0, 0))

# datetime.strptime(date_string, format)
date_string = "14 may, 2019"
print(datetime.strptime(date_string, "%d %B, %Y")) 

# datetime.strftime(format)
print(datetime.now().strftime("%d %B, %Y"))
