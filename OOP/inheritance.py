class Animal:
    def eat(self):
        print("eat")

class Mammal(Animal):  
    def walk(self):
        print("walk")
    

# Inheritance 
class Fish(Mammal):
    def swim(self):
        print("swim")
        
m = Mammal()
m.eat()
isinstance(m, Mammal)
isinstance(m, Animal)
isinstance(m, object)
    
obj = object()
obj.__doc__

print(issubclass(Mammal,Animal))