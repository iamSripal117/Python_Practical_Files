# example1
# from abc import *
# import math
#
# class MathFig(ABC):
#     def __init__(self):
#         self.dim = int(input("Enter the dimension:"))
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Circle(MathFig):
#     def __init__(self):
#         super().__init__()
#         self.radius = self.dim
#     def area(self):
#         self.aoc = 2*math.pi*self.radius
#     def perimeter(self):
#         self.poc = math.pi*self.radius
# class Square(MathFig):
#     def __init__(self):
#         super().__init__()
#         self.side = self.dim
#     def area(self):
#         self.aos = 2*self.side
#
#     def perimeter(self):
#         self.pos = 4*self.side
# c = Circle()
# c.area()
# c.perimeter()
# print("Area of Circle:",c.aoc)
# print("Perimeter of Circle:",c.poc)
#
# s = Square()
# s.area()
# s.perimeter()
# print("Area of Square:",s.aos)
# print("Perimeter of Square:",s.pos)


# example2

from abc import *
import math

class MathFig(ABC):
    def __init__(self):
        self.dim = int(input("Enter the dimension:"))
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(MathFig):
    def __init__(self):
        super().__init__()
        self.radius = self.dim
    def perimeter(self):
        self.poc = 2*math.pi*self.radius
class Ellipse(Circle):
    def area(self):
        self.aoc = math.pi*self.radius**2
class Square(MathFig):
    def __init__(self):
        super().__init__()
        self.side = self.dim
    def area(self):
        self.aos = 2*self.side

    def perimeter(self):
        self.pos = 4*self.side
e = Ellipse()
e.area()
e.perimeter()
print("Area of Circle:",e.aoc)
print("Perimeter of Circle:",e.poc)

s = Square()
s.area()
s.perimeter()
print("Area of Square:",s.aos)
print("Perimeter of Square:",s.pos)

# m = MathFig() #can't create an instance of abstract base class
# c=Circle() #can't create an instance of abstract base class