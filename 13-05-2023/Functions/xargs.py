# *args -> variable length arguments allow a function to accept number of positional arguments of any length and return a tuple


def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


# pass arguments of different length
print(multiply(2, 3))
print(multiply(2, 3, 4, 5, 6, 7, 8, 9, 10))
