# Example1 --> To know the default thread name

# from threading import *
#
# print("Default Thread Name in every python program is...",current_thread().name)

# output
# Default Thread Name in every python program is... MainThread


          #or#

# from threading import*
# if __name__ == '__main__':
#     print("Direct execution")
#     print("Default thread name is ....",current_thread().name)
# else:
#     print("Indirect execution")

# Output
# Direct execution
# Default Thread Name is....MainThread



# Example2 ---> Creating a thread without using any user defined class

# from threading import *

# def display():
#     print("Child Thread Name:",current_thread().name)
#     for i in range(1,4):
#         print("Child Thread....",i)
#
# t = Thread(target=display)
# t.start()
# print("Parent Thread Name:",current_thread().name)
# for i in range(1,4):
#     print("Parent Thread....",i)

# output
# Cant predict the output
# Note: Default name of child thread is "Thread-1"



# Example3 --->Creating a thread by extending thread class to user defined class

# from threading import*
# class MyThread(Thread):
#     def run(self):
#         print("Name of Thread Name:",current_thread().name)
#         for i in range(1,6):
#             print("Child Thread....",i)
#
# t = MyThread()
# t.start()
# print("Default Thread :",current_thread().name)
# for i in range(1,6):
#     print("Parent Thread....",i)
#
# print("Active Thread are :",active_count())

# output #
# cant predict the output

# Note: run()- method to create a block as thread and makes ready for execution thru start() method



# Example-4
# Creating a thread without extending thread class to user defined class


# from threading import*
# class MyThr:
#     def display(self):
#         print("Name of Thread Name:",current_thread().name)
#         for i in range(1,6):
#             print("Child Thread....",i)
#
# m = MyThr()
# t = Thread(target=m.display)
# t.start()
# print("Default Thread :",current_thread().name)
# for i in range(1,6):
#     print("Parent Thread....",i)
#
# print("Active Thread are :",active_count())

# OUTPUT
# cant predict the output

# active_count() ---> This method returns no.of active threads in a program


# Example -5
# Program to demonstrate a thread to sleep based on specific time and for each execution of a parent thread twice child thread are executed

# from threading import*
# import time
#
# class MyThr:
#     def display(self):
#         print("Name of Thread Name:",current_thread().name)
#         for i in range(1,6):
#             print("Child Thread....",i)
#
# m = MyThr()
# t = Thread(target=m.display)
# t.start()
# print("Default Thread :",current_thread().name)
# for i in range(1,6):
#     print("Parent Thread....",i)
#     time.sleep(2)
#
# print("Active Thread are :",active_count())

# OUTPUT
# Name of Thread Name:Default Thread : MainThread
# Parent Thread.... 1
#  Thread-1 (display)
# Child Thread.... 1
# Child Thread.... 2
# Child Thread.... 3
# Child Thread.... 4
# Child Thread.... 5
# Parent Thread.... 2
# Parent Thread.... 3
# Parent Thread.... 3
# Parent Thread.... 4
# Parent Thread.... 5
# Active Thread are : 1  #parent thread is only active in last

# Example -6
# WAP to input by one thread and output by another thread?

from threading import*
import time

# class MyThread(Thread):
#
#     def __init__(self):
#         super().__init__()
#         self.msg = "sripal"
#     def run(self):
#         print("Child Thread name:", current_thread().name)
#         while True:
#             print(self.msg)
#             time.sleep(1)
# print("Parent thread",current_thread().name)
# t = MyThread()
# t.start()
# while True:
#     s = input()
#     t.msg = s

# OUTPUT
# Parent thread MainThread
# Child Thread name: Thread-1
# sripal
# sripal
# sripal


