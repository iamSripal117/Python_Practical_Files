######################################################Class############################

##Example1:

##class Demo:
##    '''class designed for demonstration'''
##    a=12  # static attribute / public attribute(variable)/data members/field  
##    _b=23 # static attribute / protected attribute(variable)/data members/field
##    __c=222 # static attribute / private attribute(variable)/data members/field
##
##    print(" In class:",a)
##    print(" In class:",_b)
##    print(" In class:",__c) # no need of name mangling when you are printing attrtibute in class
##    
##
##print(Demo.__doc__)
##print(Demo.__dict__)
##print(Demo.__name__)
##print(Demo.__class__)
##print(Demo.__module__)
##print(Demo.__base__)
##print(Demo.__bases__)
##print(Demo.a)
##print(Demo._b)
####print(Demo.__c) # attribute error
##print(Demo._Demo__c) # this is called "name mangling" we use this name magling only outside the class.


##(OUTPUT)###### example1
##In class: 12
## In class: 23
## In class: 222
##class designed for demonstration
##{'__module__': '__main__', '__doc__': 'class designed for demonstration', 'a': 12, '_b': 23, '_Demo__c': 222, '__dict__': <attribute '__dict__' of 'Demo' objects>, '__weakref__': <attribute '__weakref__' of 'Demo' objects>}
##Demo
##<class 'type'>
##__main__
##<class 'object'>
##(<class 'object'>,)
##12
##23




##Example 2


##class Sample:
##    a=18
##    b=2.4
##    c=True
##    d="Python"
##
##print(type(Sample))
##print(id(Sample))
##print(Sample.__dict__)
##print(Sample.a,"",Sample.b,"",Sample.c,"",Sample.d) # all attributes printing in one line


##########OUTPUT(Example2)########
##<class 'type'>
##2219886882320
##{'__module__': '__main__', 'a': 18, 'b': 2.4, 'c': True, 'd': 'Python', '__dict__': <attribute '__dict__' of 'Sample' objects>, '__weakref__': <attribute '__weakref__' of 'Sample' objects>, '__doc__': None}
##18  2.4  True  Python


###############################################objects##############################







#######self --(parameter)##########

##class Demo:
##    def show(self):
##        print("From show method:")
##    def display(s):       #  s works for self # you can change self to anything like alphabet 
##        print ("From display method:")
##        s.show()
##d = Demo()
####print(Demo.__dict__)
####print(d.__dict__)
##d.display()
##d.show()



########Example for creating instance variables############
##Example 1:


##class Employ:
##    def get_data(self):
##        self.emp_id = int(input("Enter the Id:"))
##        self.emp_name = input("Enter the emp name:")
##        self.emp_sal = float(input("Enter the emp salary:" ))
##    def calc_sal(self):
##        self.annual_sal= self.emp_sal*12
##    def display(self):
##        print("Emply Id:",self.emp_id)
##        print("Emply name:",self.emp_name)
##        print("Emply sal:",self.emp_sal)
##        print("Annual salary:",self.annual_sal)
##e = Employ()                #creating instance
##e.get_data()
##e.calc_sal()
##e.display()
##print(e.emp_id,e.emp_name,e.emp_sal,e.annual_sal)

##########OUTPUT example-1 of self,object,class#########
##Enter the Id:1234
##Enter the emp name:sripal
##Enter the emp salary:12000
##Emply Id: 1234
##Emply name: sripal
##Emply sal: 12000.0
##Annual salary: 144000.0
##1234 sripal 12000.0 144000.0


############Example for working with local variables############


##Example 1:

##class Sample:
##    x=21 # public attribute
##    def get_value(self):
##        self.b=22 #instance variable
##        r=33 # local variable
##        print("local variable:",r)
##        print("instance variable:",self.b)
##b=Sample()
##b.get_value()
##print("public attribute:",Sample.x)

##############OUTPUT##############
##local variable: 33
##instance variable: 22
##public attribute: 22



##example 2 : (parameter and argument passing)

##class Demo:
##    def display(self,s,r,t):
##        print("sum of",s,"and",r,"is",t)
##         
##    def calc(self,x,y):
##        z=x+y
##        self.display(x,y,z)
##    def get_values(self):
##        a=int(input("Enter the a value:"))
##        b=int(input("Enter thr b value:"))
##        self.calc(a,b)
##
##pa = Demo()
##pa.get_values()              


########################OUTPUT (example 2)#########
##Enter the a value:23
##Enter thr b value:45
##sum of 23 and 45 is 68






##passing objects from one class to anothe class##

##
##class Employ:
##    def __init__(self):
##        self.Emp_Id = 0
##        self.Emp_name = ""
##        self.Emp_sal = 0.0
##        
##    def get_info(self):
##        self.Emp_Id = int(input("enter the id:"))
##        self.Emp_name = input("enter the name:")
##        self.Emp_sal = float(input("enter the sal:"))
##
##class Personal:
##    def __init__(self):
##        self.ann_sal = 0.0
##    def calc(self,emp):
##        self.ann_sal= emp.Emp_sal*12
##        print("Employ ID:",emp.Emp_Id)
##        print("Employ name:",emp.Emp_name)
##        print("Employ sal:",emp.Emp_sal)
##        print("Annual sal:",self.ann_sal)
##e = Employ()
##e.get_info()
##p= Personal()
##p.calc(e)
##        

##########OUTPUT############
################################################enter the id:12
################################################enter the name:sripal
################################################enter the sal:24000
################################################Employ ID: 12
################################################Employ name: sripal
################################################Employ sal: 24000.0
################################################Annual sal: 288000.0




######INNER CLASS (contained object)##########
##
##class Company: #outer class
##    def __init__(self):
##        self.cname=''
##    def get_comp_name(self):
##        self.cname = input("Enter the company name:")
##    def show_comp_name(self):
##        print("Company name is :",self.cname)
##    class Employee:
##        def __init__(self):
##            self.ename = ''
##        def get_ename(self):
##            self.ename = input("Enter the employee name:")
##        def show_ename(self):
##            print("Employee name is :",self.ename)
##c = Company()
##s = Company.Employee()
##c.get_comp_name()
##s.get_ename()
##c.show_comp_name()
##s.show_ename()

####output####
################################Enter the company name:RSTech
################################Enter the employee name:Sripal
################################Company name is : RSTech
################################Employee name is : Sripal

###### OR ######

##class Company: #outer class
##    def __init__(self):
##        self.cname=''
##    def get_comp_name(self):
##        self.cname = input("Enter the company name:")
##        self.e.get_name()
##    def show_comp_name(self):
##        print("Company name is :",self.cname)
##        self.e.show_name()
##    class Employee:
##        def __init__(self):
##            self.ename = ''
##        def get_ename(self):
##            self.ename = input("Enter the employee name:")
##        def show_ename(self):
##            print("Employee name is :",self.ename)
##    e = Employee()        
##c = Company()
####c.get_comp_name()
####c.show_comp_name()

##############OUTPUT###########
####################################Enter the company name:RSTech
####################################Enter the employee name:Sripal
####################################Company name is : RSTech
####################################Employee name is : Sripal


















        
























        
    
























    









































    
