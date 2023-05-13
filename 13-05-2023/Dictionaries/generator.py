from sys import getsizeof  

values = (x*2 for x in range(10000))
print(values) 
for value in values:
    print(value)
    
print("gen:", getsizeof(values))

values = [x*2 for x in range(10000)]
print("list:", getsizeof(values))