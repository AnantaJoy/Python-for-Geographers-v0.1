class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): # __str__ is a special method
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        

point = Point(1, 2)
point.draw()
print(point) # print() calls str() on the object