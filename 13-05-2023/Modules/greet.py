# A file containing a set of functions you want to include in your application.
import platform
from test_module import greeting
import test_module as tm
import test_module

test_module.greeting()

name = test_module.student_info["name"]
print(name)

# alias

tm.greeting()

age = tm.student_info["age"]
print(age)

# import specific items

greeting()

# buit-in modules

x = platform.system()
print(x)
