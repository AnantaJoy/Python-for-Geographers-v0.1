# getter and setter


class Product:
    def __init__(self, price):
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be positive")
        self.__price = value




        