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










