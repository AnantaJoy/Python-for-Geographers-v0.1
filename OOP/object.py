class StudentInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    

student = StudentInfo("John", 20)
print(student.get_name())
print(student.get_age())
print(isinstance(student, StudentInfo))
print(isinstance(student, int))