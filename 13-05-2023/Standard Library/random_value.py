import random 

# Generate a random number between 0 and 1
value = random.random()
print(value)

# Generate a random integer between 1 and 10
value = random.randint(1, 10)
print(value)

# Generate a random integer between 0 and 10
value = random.randrange(10)
print(value)

# Generate a random integer between 0 and 100 (even numbers only)
value = random.randrange(0, 101, 2)
print(value)

# choice random value from an array
greetings = ["Hello", "Hi", "Hey", "Howdy", "Hola"]
value = random.choice(greetings)
print(value)

# choice random value from a string
value = random.choice("Hello")
print(value)

# choice random value from a tuple
value = random.choice((1, 2, 3, 4, 5))
print(value)

# choices random value from list
colors = ["Red", "Black", "Green"]
results = random.choices(colors, k=10)
print(results)

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.capwords("hello world"))

# generate a random password
password_genrator = string.ascii_letters + string.digits + string.punctuation
password = random.choices(password_genrator, k=15)
print("".join(password))