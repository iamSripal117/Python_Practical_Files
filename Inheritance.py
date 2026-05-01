##Inheritance==it is a process of creating a new class form existing class is called inheritance

##Single Inheritance##

##class Demo:
##    pass
##class Sample(Demo):
##    pass
##





######points to be remembered when working with inheritance######

##1.every class created in python by default it is child class of object class.....<class 'object'>

##class Demo:
##    pass
##class Sample(Demo):
##    pass
##class Test:
##    pass
##class Student:
##    pass
##print(Demo.__base__)
##print(Sample.__base__)
##print(Sample.__bases__)
##print(Test.__base__)
##print(Student.__base__)

######OUTPUT######
##########################<class 'object'>
##########################<class '__main__.Demo'>
##########################(<class '__main__.Demo'>,)
##########################<class 'object'>
##########################<class 'object'>





####2.When instance of derived class is created it will allocate memory to all the members of base and derived class whereas if instance of base class is
####created then it will allocate memory to only members of base class.


####example

# class B1:
#     def show(self):
#         self.a = 10
# class D1(B1):
#     def display(self):
#         self.b = 15
# d=D1()
# d.show()
# d.display()
# print(d.__dict__) #{'a': 10, 'b': 15}
#
# b=B1()
# b.show()
# b.display() #AttributeError
# print(b.__dict__) #{'a': 10}


# 6.Python doesn't support overriding of instance and class variables:

class B1:
    x=20
    def show(self):
        print("From show of base")
        self.a = 10
class D1(B1):
    x=22
    def show(self):
        print("From show of Derived")
        self.a = 34
        print("Before base show",self.a)
        super().show()
        print("After base show",self.a)

d = D1()
d.show()
print(d.__dict__)
print(B1.__dict__)
print(D1.__dict__)

























