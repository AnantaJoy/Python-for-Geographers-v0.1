# **kwargs -> arbitrary keyword arguments allow a function to accept number of keyword arguments of any length and return a dictionary

def save_user(**user):
    print(user)
    print(user["name"])
    
save_user(id=1, name="John", age=22)
# Output: {'id': 1, 'name': 'John', 'age': 22}

 
# create user info dictionary

def create_user_info(name,**kwargs):
    user_info = {}
    user_info["name"] = name
    for key, value in kwargs.items():
        user_info[key] = value
    return user_info

user1 = create_user_info("John", age=22, city="New York", country="USA")
print(user1)
# Output: {'name': 'John', 'age': 22, 'city': 'New York', 'country': 'USA'}

user2 = create_user_info("Jane", age=21, city="London", country="UK", phone="1234567890")
print(user2)
# Output: {'name': 'Jane', 'age': 21, 'city': 'London', 'country': 'UK', 'phone': '1234567890'}

user3 = create_user_info("Bob", age=21, city="Dhaka", country=" Bangladesh", phone="1234567890", email="xyz@example.com")
print(user3)