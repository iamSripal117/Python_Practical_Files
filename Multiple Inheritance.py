# Example 1
# class B1:
#     def x(self):
#         print("From x method of Base class")
# class B2:
#     def y(self):
#         print("From y method of Base class")
# class D1(B1,B2):
#     def z(self):
#         print("From z method of Derived class")
# d = D1()
# d.x()
# d.y()
# d.z()

# Example 2.1
# class B1:
#     def x(self):
#         print("From x method of B1 class")
# class B2:
#     def x(self):
#         print("From x method of B2 class")
# class D1(B1,B2): #priority one execute first in this base classes methods
#     def z(self):
#         print("From z method of Derived class")
# d = D1()
# d.x()  #B1 class method execute
# d.z()  #D1 class method execute

# Example 2.2 #
class B1:
    def x(self):
        print("From x method of B1 class")
class B2:
    def x(self):
        print("From x method of B2 class")
class D1(B2,B1): #priority one execute first in this base classes methods
    def z(self):
        print("From z method of Derived class")
d = D1()
d.x() #From x method of B2 class
d.z() #From z method of Derived class















