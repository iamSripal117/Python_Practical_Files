# base class is inherited to more than one derived class
# creates tree format


# Example1#

# class Vehicle:
#     def __init__(self):
#         self.fuel = input("Enter the fuel:")
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print("Fuel of car is....",self.fuel)
# class Scooter(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print("Fuel of scooter is....",self.fuel)
# print("For Car")
# c = Car()
# print("For Scooter")
# s = Scooter()

# Example 2 #

# class Vehicle:
#     def __init__(self,cn):
#         print(f"Enter the fuel for {cn}:",end='')
#         self.fuel = input()
# class Car(Vehicle):
#     def __init__(self,cn):
#         super().__init__(cn)
#         print("Fuel of car is....",self.fuel)
# class Scooter(Vehicle):
#     def __init__(self,cn):
#         super().__init__(cn)
#         print("Fuel of scooter is....",self.fuel)
# c = Car(Car.__name__)
# s = Scooter(Scooter.__name__)
