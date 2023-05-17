import time

# list comprehension
start = time.time()
list1 = [i**2 for i in range(10000000)]
end = time.time()
print(end - start)

# generator expression
start = time.time()
list2 = (i**2 for i in range(10000000))
end = time.time()
print(end - start)
