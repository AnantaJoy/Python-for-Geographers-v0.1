months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November','December']
days = [31,28,31,30,31,30,31,31,30,31,30,31]
print(zip(months, days))

for month in zip(months, days):
    print(f'{month[0]} has {month[1]} days')