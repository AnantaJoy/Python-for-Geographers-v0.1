
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    print(month)
    
    
for month in months:
    print(month, end=' ')
    print("\n")
    
for month in enumerate(months):
    print(month)
    
for index, month in enumerate(months):
    print(index+1, month)