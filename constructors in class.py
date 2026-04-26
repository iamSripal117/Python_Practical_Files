


            ###PARAMETERLESS CONSTRUCTOR###

##Example 1: parameterless constructor / default constructor
##
##class Employ:
##   def __init__(self):
##       print("In constructor")
##       self.emp_id= None
##       self.emp_name=None
##       self.emp_sal= None
##       self.annual_sal= None
##   def all_data(self):
##       self.emp_id=int(input("Enter the id:"))
##       self.emp_name =input("Enter thr name:")
##       self.emp_sal =float(input("Enter the sal:"))
##   def calc(self):
##       self.annual_sal=self.emp_sal*12
##
##   def display(self):
##       print(self.emp_id)
##       print(self.emp_name)
##       print(self.emp_sal)
##       print(self.annual_sal)
##e = Employ()
##e.all_data()
##e.calc()
##e.display()




##############    Output ######################

##In constructor
##Enter the id:3456
##Enter thr name:sdfghj
##Enter the sal:24000
##3456
##sdfghj
##24000.0
##288000.0








                    ##PARAMETERIZED CONSTRUCTOR##

######Example-2:WAP to demonstrate parameterized constructor    ############


##class Sample:
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##        self.z= None
##    def calc(self):
##        self.z= self.x+self.y
##    def display(self):
##        print(f"Sum of{self.x}and{self.y} is {self.z}")
##a=int(input("Enter the value of a:"))
##b= int(input("Enter the value of b:"))
##c=Sample(a,b) #named Instance(object)
##c.calc()
##c.display()
        

       #(OR)

##class Sample:
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##        self.z= None
##        self.calc()
##    def calc(self):
##        self.z= self.x+self.y
##        self.display()
##    def display(self):
##        print(f"Sum of {self.x} and {self.y} is {self.z}")
##a=int(input("Enter the value of a:"))
##b= int(input("Enter the value of b:"))
##Sample(a,b) #nameless Instance(object) / Anonymous object

############## OUTPUT Example-2##############

##Enter the value of a:23
##Enter the value of b:23
##Sum of 23 and 23 is 46











############Example -3: WAP to to count no.of instances in the class  ##########

##class Demo:
##    count =0
##    def __init__(self):
##        Demo.count +=1
##Demo()
##Demo()
##Demo()
##Demo()
##Demo()
##Demo()
##
##print(f"No.of times instances repeated is {Demo.count}")


              #OR

##class Demo:
##    count =0
##    def __init__(self):
##        Demo.count +=1
##[Demo(),Demo(),Demo(),Demo(),Demo(),Demo()]   #you can also mention the instance in list
##
##print(f"No.of times instance repeated is {Demo.count}")

####################   OUTPUT    ####################
## No.of times instance repeated is 6



############Example -4 #############

##WAP to count number of references created for an instance of a class?

import sys
class Demo:
    def show(self):
        print("I am the show method in Demo class")
d=Demo()
d1 =d
d2 = d
d3 = d
print(id(d),id(d1),id(d2),id(d3))
print("No.of referneces created for the instance including default ref is ....",sys.getrefcount(d))
print("No.of referneces created for the instance excluding default ref is ....",sys.getrefcount(d)-1)




































        

