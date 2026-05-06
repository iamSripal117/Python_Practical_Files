# 1.Simple Version #

# Example 1
# n=int(input("Enter a number: "))
# assert n>0
# print("Entered n value is +ve") #if n positive this will print
# if n is negative AssertionError

# 2.augmented version
# assert conditional_expression,msg

# 1 way
# n=int(input("Enter a number: "))
# assert n>0,"Entered n value is -ve or Zero"
# print("Entered n value is +ve")

               #(or)

# 2nd way with try and except blocks
# try:
#     n=int(input("Enter a number: "))
#     assert n>0,"Entered n value is -ve or Zero"
#     print("Entered n value is +ve")
# except AssertionError as msg:
#     print(msg)


# Example3

# def square(n):
#     return n*n
#
# assert square(5) == 25 ,"square of 5 is 25"
# assert square(10) == 100 ,"square of 10 is 100"
# assert square(20) == 400 ,"square of 20 is 400"
# print(square(5))
# print(square(10))
# print(square(20))