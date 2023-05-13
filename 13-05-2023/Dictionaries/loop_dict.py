dept_name = {"CS": "Computer Science","EE" :"Electrial and Electronic" ,"MATH": "Mathematics", "STAT": "Statistics"}

# Looping through the keys
for key in dept_name:
    print(key)
    
# Looping through the values
for value in dept_name.values():
    print(value)
    
# Looping through the key-value pairs
for key, value in dept_name.items():
    print(key,":",value)