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

# try:
#     x = int(input("enter number:"))
#     y = int(input("enter number:"))
#     # a = int(input("enter number:"))
#     z = x / y
#     print(f"the div of {x} and {y} is {z}")
# except:
#     print("number or data type error")
# finally:
#     print("code executed")
#
# try:
#     x = int(input("enter number:"))
#
# except:
#     print("value error")
# finally:
#     print("code executed")

# example-6: Handling all the exceptions using a base class called BaseException

# try:
#     a = int(input("Enter a :"))
#     b = int(input("Enter b :"))
#     c = a/b
#     print(c)
# except BaseException as e:
#     print("Exception handled:",e)
# finally:
#     print("End of the program")


# example-7:child class(any Error) exception after base class(BaseException) exception

# try:
#     x = int(input("enter number:"))
#     y = int(input("enter number:"))
#     a = int(input("enter number:"))
#     z = x / y
#     print(f"the div of {x} and {y} is {z}")
# except BaseException as e:
#     print("Exception Handled by base class :",e)
# except ZeroDivisionError:
#     print("division by zero")
# finally:
#     print("code executed")



# example-8: child class exception before base class

# try:
#     x = int(input("enter number:"))
#     y = int(input("enter number:"))
#     a = int(input("enter number:"))
#     z = x / y
#     print(f"the div of {x} and {y} is {z}")
# except ZeroDivisionError:
#     print("division by zero")
# except BaseException as e:
#     print("Exception Handled by base class :",e)
# finally:
#     print("code executed")


# Example-9  Using "Exception" for all the exceptions including parent class

# try:
#     x = int(input("enter number:"))
#     y = int(input("enter number:"))
#     a = int(input("enter number:"))
#     z = x / y
#     print(f"the div of {x} and {y} is {z}")
# except Exception as e:
#     print("Exception Handled by exception :",e)
# # except BaseException as e:
# #     print("Exception Handled by base class :",e)
# finally:
#     print("code executed")


# Example-10: "Raise" Raising built-in exceptions manually pre call to an exception

try:
    x = int(input("enter number:"))
    y = int(input("enter number:"))
    if y == 0:
        raise ZeroDivisionError
    z = x/y
    print(f"the div of {x} and {y} is {z}")
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("code executed")