from abc import ABC, abstractmethod                           

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius
        
rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.area()}")       
print(f"Perimeter: {rectangle.perimeter()}\n\n") 

circle = Circle(7)
print(f"Area: {circle.area()}")       
print(f"Perimeter: {circle.perimeter()}")
