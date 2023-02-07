from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def cal(self, a, b):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def cal(self, a, b):
        return a + b

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius**2

    def cal(self, a, b, c):
        return a * b * c

shapes = [Rectangle(10, 20), Circle(30), Circle(40), Rectangle(50, 60)]

for shape in shapes:
    print(f'area of shape is {type(shape)} {shape.area()}')

r = Rectangle(10, 20)
c = Circle(20)
print(r.cal(10, 20))
print(c.cal(10, 2, 3))