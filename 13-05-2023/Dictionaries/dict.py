student_info = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student_info)

# using dict constructor
student_info = dict(name="John", age=25, courses=["Math", "CompSci"])
print(student_info)

# Getting the keys
print(student_info.keys())

# Getting the values
print(student_info.values())

# Accessing a value
print(student_info["name"])

# Accessing a value using get method
print(student_info.get("name"))

# Accessing a value that does not exist
# print(student_info["phone"]) # KeyError: 'phone'
# print(student_info.get("phone")) # None

# Accessing a value that does not exist with a default value
print(student_info.get("phone", "Not Found"))

# Adding a new key-value pair
student_info["phone"] = "555-5555"
print(student_info)

# Updating a key-value pair
student_info["name"] = "Jane"
print(student_info)

# Updating a key-value pair using update method
student_info.update({"name": "Jane", "age": 26, "phone": "555-5555"})
print(student_info)

# Deleting a key-value pair
del student_info["phone"]
print(student_info)

# Deleting a key-value pair using pop method
age = student_info.pop("age")
print(student_info)

# Getting the number of key-value pairs
print(len(student_info))

