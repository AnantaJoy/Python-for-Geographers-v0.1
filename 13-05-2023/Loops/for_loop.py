# print 1-10 using for loop
for i in range(1, 11):
    print(i)
# similar result as above
for i in range(10):
    print(i)
    
# looping through a range of numbers with a step of 2
for i in range(1, 11, 2):
    print(i)

# looping over a string
for i in "Hello":
    print(i)
    

# loop through all of the elements of a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit.title())


# sum of all the numbers in a list
numbers = [1, 2, 3, 4, 5]
sum = 0

for number in numbers:
    sum += number
    
print(sum)