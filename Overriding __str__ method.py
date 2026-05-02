class Employ:
    def __init__(self):
        self.emp_id = 0
        self.e_name = ''
        self.salary = 0.0
    def get_emp_details(self):
        self.emp_id = int(input('Enter emp id: '))
        self.e_name = input('Enter emp name: ')
        self.salary = float(input('Enter salary: '))
    def __str__(self):
        return f'Employee Id: {int(self.emp_id)} \nEmployee name: {self.e_name} \nEmployee salary: {float(self.salary)}'
e = Employ()
e.get_emp_details()
# print(e) ---> when __str__ is not overridden then by default it displays reference of object but not values of instance variables

print(e)
print(e.__str__())
