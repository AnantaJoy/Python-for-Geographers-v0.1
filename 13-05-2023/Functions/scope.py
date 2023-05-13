# local and global variables
# local scope is used to determine the variable inside the function and global scope is used to determine the variable outside the function

global_var = "This is a global variable"

def func():
    print(global_var)
    local_var = "This is a local variable"
    print(local_var)
    

func()
# Output: This is a global variable
#         This is a local variable

print(global_var)   # Output: This is a global variable
# print(local_var)    # Output: NameError: name 'local_var' is not defined

# global keyword
# global keyword is used to create a global variable inside a function

def func():
    global local_var
    local_var = "This is a local variable"
    
func()
# Output: This is a global variable

print(local_var)