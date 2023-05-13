# keyword arguments are arguments that are passed into a function with a key and a value

def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')

# positional arguments
greet_user('Jesse', 'Smith')

# keyword arguments
greet_user(last_name='Smith', first_name='Jesse')

# keyword arguments are useful when you have a function with many parameters
# and you want to specify which parameter is which


