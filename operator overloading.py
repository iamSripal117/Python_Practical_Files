# Example-1
# class Demo:
#     def __init__(self):
#         self.val = int(input('Enter a number: '))
#
#     def __add__(self, other):   #magic methods
#         return self.val + other.val
#     def __sub__(self, other):    # magic methods
#         return self.val - other.val
#     def __mul__(self, other):    #magic methods
#         return self.val * other.val
#     def __truediv__(self, other):   # magic methods
#         return self.val / other.val
#
# d1 = Demo()
# d2 = Demo()
# res = d1 + d2
# print(f"sum of {d1.val} and {d2.val} is {res}")
# res = d1 - d2
# print(f"difference of {d1.val} and {d2.val} is {res}")
# res = d1 * d2
# print(f"multiplication of {d1.val} and {d2.val} is {res}")
# res = d1 / d2
# print(f"division of {d1.val} and {d2.val} is {int(res)}")


# example-2
# perform concatenation and addition of values stored in 2 objects?

# class Demo:
#     def __init__(self):
#         self.val = input('Enter a number: ')
#
#     def __add__(self, other):   #magic methods  # add operator should concat here
#         if str.isnumeric(self.val) and str.isnumeric(other.val):  # isnumeric will convert str to integer
#             return int(self.val) + int(other.val)
#         else:
#             return self.val + other.val
#
#
# d1 = Demo()
# d2 = Demo()
# res = d1 + d2
# print(res)


# example-3:

# class Demo:
#     def __init__(self):
#         self.val = int(input('Enter a number: '))
#
#     def __gt__(self, other):   #magic methods
#         if self.val > other.val:
#             return self.val
#         else:
#             return self.val
#
#
#
# d1 = Demo()
# d2 = Demo()
# res = d1 > d2
# print(" both values are equal :",res)


# example-4

# creating a nested list in 2 objects

class MatAdd:
    def __init__(self):
        self.lst =[]
        self.nlst =[]
    def get_values(self):
        for i in range(3):
            self.lst =[]
            for j in range(3):
                ele = int(input(f"Enter value for {i} row and {j} col :"))
                self.lst.append(ele)
            self.nlst.append(self.lst)
    def show_values(self):
        for i in range(3):
            for j in range(3):
                print(self.nlst[i][j],end="\t ")
            print()
    def __add__(self,other):
        self.nres =[]
        for i in range(3):
            self.res = []
            for j in range(3):
                self.a = self.nlst[i][j] + other.nlst[i][j]
                self.res.append(self.a)
            self.nres.append(self.res)
        return self.nres
m1 = MatAdd()
m2 = MatAdd()
print("enter 9 values for 1st matrix")
m1.get_values()
print("enter 9 values for 2nd matrix")
m2.get_values()
m3 = m1 + m2
print("1st matrix")
m1.show_values()
print("2nd matrix")
m2.show_values()
print("Resultant Matrix")
for i in range(3):
    for j in range(3):
        print(m3[i][j],end=" \t ")
    print()









