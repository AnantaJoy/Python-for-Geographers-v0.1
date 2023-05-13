try:
    age = int(input("Enter age: "))
except ValueError as ex:
    print("Invalid value")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
    
print("Execution continues........ ")

