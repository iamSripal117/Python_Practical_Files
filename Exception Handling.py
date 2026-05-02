# IN EXCEPTION HANDLING #

# only try block ---invalid
# try finally block ---valid
# try  2-finally blocks ---not valid
# try except finally ---valid
# try 2-except blocks finally ---valid
# try 2-except blocks ---valid


# example 1 (only try finally blocks)
# try:
#   x = int(input("enter number:"))
#   y = int(input("enter number:"))
#   a = int(input("enter number:"))
#   z = x / y
#   print(f"the div of {x} and {y} is {z}")
# finally:
#     print("The program ends")
#

# example 2 (try except finally blocks)
# only one except
# try:
#   x = int(input("enter number:"))
#   y = int(input("enter number:"))
#   a = int(input("enter number:"))
#   z = x / y
#   print(f"the div of {x} and {y} is {z}")
# except ZeroDivisionError:
#   print(" number error")
# finally:
#     print("The program ends")


# example-3 (using try except...except finally blocks)
# multiple except
# try:
#   x = int(input("enter number:"))
#   y = int(input("enter number:"))
#   a = int(input("enter number:"))
#   z = x / y
#   print(f"the div of {x} and {y} is {z}")
# except ZeroDivisionError:
#   print("number error")
# except ValueError:
#     print("data type error")
# finally:
#     print("The program ends")


# example-4 (using try except(multi errors) finally blocks)
# multiple except
# try:
#     x = int(input("enter number:"))
#     y = int(input("enter number:"))
#     # a = int(input("enter number:"))
#     z = x / y
#     print(f"the div of {x} and {y} is {z}")
# except (ZeroDivisionError, ValueError):
#     print("number or data type error")
# finally:
#     print("code executed")


# example-5

try:
    x = int(input("enter number:"))
    y = int(input("enter number:"))
    # a = int(input("enter number:"))
    z = x / y
    print(f"the div of {x} and {y} is {z}")
except:
    print("number or data type error")
finally:
    print("code executed")
