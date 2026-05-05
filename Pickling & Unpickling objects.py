# Example-1: Pickling and Unpickling single objects

# pickling single object #

# import pickle
# class Employee:
#     def __init__(self):
#         self.emp_Id = 0
#         self.name = ""
#         self.salary = 0.0
#     def display(self):
#         self.emp_Id = int(input("enter emp id:"))
#         self.name = input("enter name:")
#         self.salary = float(input("enter salary:"))
# e = Employee()
# e.display()
# f=open("employee.dat","wb")
# pickle.dump(e, f) #pickling
# f.close()



# Unpickling single object #

# import pickle
# class Employee:
#     def __init__(self):
#         self.emp_Id = 0
#         self.name = ""
#         self.salary = 0.0
#     def display(self):
#         print("Employee Id:",self.emp_Id)
#         print("name:",self.name)
#         print("salary:",self.salary)
# f = open("employee.dat","rb")
# obj = pickle.load(f) #Unpickling object
# obj.display()
# f.close()

# Example -2: Pickling and Unpickling multiple objects

# Pickling Multiple Objects

import pickle
class Employee:
    def __init__(self):
        self.emp_Id = 0
        self.name = ""
        self.salary = 0.0
    def display(self):
        self.emp_Id = int(input("enter emp id:"))
        self.name = input("enter name:")
        self.salary = float(input("enter salary:"))
f = open("emp.txt","wb")
opt = "yes"
while opt == "yes":
    e = Employee()
    e.display()
    pickle.dump(e, f) #pickling
    opt = input("do you want to continue?(yes/no):")
f.close()



# Unpickling Multiple Objects

# import pickle
# class Employee:
#     def __init__(self):
#         self.emp_Id = 0
#         self.name = ""
#         self.salary = 0.0
#     def display(self):
#         print("Employee Id:",self.emp_Id)
#         print("name:",self.name)
#         print("salary:",self.salary)
# try:
#    f = open("emp.txt","rb")
#    while True: #unpickling
#        obj = pickle.load(f)
#        obj.display()
# except EOFError: #EndOfFileError
#    print("All data accessed")
# finally:
#       f.close()


























