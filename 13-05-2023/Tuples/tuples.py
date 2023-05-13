# Tuples are immutable means you can't change the values of tuple

# creating a tuple
number = 1,
print(type(number))
number = 1,2
print(type(number))

number = (1,2,3)
print(type(number))

# using tuple constructor
number = tuple((1,2,3))
print(type(number))

# multiple values
number = (1,2,3)*3
print((number))

# list to tuple
age = [35,45]
print(tuple(age))
print(tuple("hello"))

# accessing tuple
print(number[0])
print(number[0:2])

# unpacking tuple
point = (1,2,3)
x,y,z = point
print(x)
print(y)
print(z)

ages = (35,45,55,65)
person1, *person2, person3 = ages
print(person2)