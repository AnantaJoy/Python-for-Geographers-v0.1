# print(iter(123))

# check wheather it iterable 

def check_iterable(iterable):
    try:
        iter(iterable)
        return True
    except TypeError:
        return False

print(check_iterable(123))
print(check_iterable("Hello"))
print(check_iterable([1, 2, 3]))
print(check_iterable({"name": "John", "age": 36}))
print(check_iterable((1, 2, 3)))
print(check_iterable(3.4))
print(check_iterable(True))