dept_name = ['EEE','CSE','ME','CE','TE','IPE','BBA','ARCHI']

first, second, third, fourth, fifth, sixth, seventh, eighth = dept_name
print(first)
# first, second, third, fourth, fifth, sixth, seventh, eighth, nineth = dept_name
# print(nineth)
first, second, *others = dept_name
print(others)
first, *others, last = dept_name
print(others)
print(last)