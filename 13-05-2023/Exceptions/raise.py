# raise exception with argument and without argument


def age_validate(age):
    if age <= 0:
        raise ValueError("Age can not be less than or equal to zero")
    else:
        print("Age is valid")

try:    
    age_validate(0)
except ValueError as e:
    print(e)