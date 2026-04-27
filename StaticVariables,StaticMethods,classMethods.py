##Static Variables or Static Attributes
##These variables are created in a class and to access them you need to use class namt to it

##Example 1:

##class Sample:
##    a=20 #static variable
##    def show(self):
##        Sample.a = Sample.a + 10 #30
##        self.b = 10
##
##    def display(self):
##        Sample.a = Sample.a + 15 #45
##s1 = Sample()
##s2 = Sample()
##s1.show() # adds 45  to 10 == 55
##s1.display() # adds 55 to 15 ==70
####s2.show()  # this adds 70 + static variable 20
####s2.display()
####s2.b = s2.b + 10 #20
####Sample.a = Sample.a + 20 #90
##
####print(s1.a, '\t', s1.b, '\t', Sample.a)
####print(s2.a, '\t', s2.b, '\t', Sample.a)
##
##print(s1.a)
##print(Sample.a)


        
##########################   Example 2  ############

##class Sample:
##    a = 10 #static variable
##    def show(self):
##        self.a = self.a + 10
##    def display(self):
##        self.a = self.a + 10
##s1 = Sample()
##s1.show()
##s1.show()
##print("Instance variable value is:",s1.a)
##print("Static variable variable value is:",Sample.a)


############Static Methods and class methods###############

class Demo:
    a = 70 #static variable

    @staticmethod  # doesn't need any parameter
    def show():
        print("In static show method")
        Demo.a = Demo.a + 10  #static variiable using class name 
        
    @classmethod   # we use cls as parameter and we use (cls)instead of class name to declare a static variable
    def display(cls):
        print("In class method")
        print(type(cls))
        cls.a = cls.a +10   # classmethod static variable with clas name as "cls"
        Demo.a = Demo.a +10 
print(type(Demo))
d = Demo()
d.show()
d.display()
d.a = d.a +100
print("Static variable is ....", Demo.a,d.a)





































