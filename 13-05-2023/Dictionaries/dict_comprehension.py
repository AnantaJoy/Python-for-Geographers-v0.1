values = []
 
for i in range(10):
    values.append(i)

print(values)

# list comprehension
values = [i for i in range(10)]
print(values)

# set comprehension
values = {i for i in range(10)}
print(values)

# dict comprehension
values = {i: i * 2 for i in range(10)}
print(values)