class Employee:
    def greet(self):
        print("Employee greeting")

class Person:
    def greet(self):
        print("Person greeting")

class Manager(Person, Employee):
    pass

manager = Manager()
manager.greet()