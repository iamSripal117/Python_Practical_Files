class InvalidSalaryExcep(BaseException):
      def __init__(self,sal):
          self.pay = salary
      def __str__(self):
          return "Salary cant be zero " + str(self.pay)

try:
   empid = int(input("enter number:"))
   ename = input("enter name:")
   salary = float(input("enter number:"))
   if salary<0:
       raise InvalidSalaryExcep(salary)
   print("Employee id:",empid)
   print("Employee name:", ename)
   print("Salary:",salary)
except InvalidSalaryExcep as e:
    print(e)
