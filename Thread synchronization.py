# Example-1
# Without Synchronization

from threading import *
import time
def show(name):
    for i in range(3):
        if name == "sripal":
            print(name)
            time.sleep(1)
        else:
            print(name)
            time.sleep(1)
t1 = Thread(target=show, args=("sripal",))
t2 = Thread(target=show, args=("reddy",))
t1.start()
t2.start()

# output
# Cant predict the output


# Example-2
# With Synchronization:

# from threading import *
# import time
#
# lck=Lock()
#
# def show(name):
#     for i in range(3):
#         lck.acquire()
#         if name == "sripal":
#             print("Hello.....",end='')
#             time.sleep(2)
#             print(name)
#         else:
#             print("Hiii!!.....",end='')
#             time.sleep(2)
#             print(name)
#         lck.release()
# t1 = Thread(target=show, args=("sripal",))
# t2 = Thread(target=show, args=("reddy",))
# t1.start()
# t2.start()

# output
# Hello.....sripal
# Hello.....sripal
# Hello.....sripal
# Hiii!!.....reddy
# Hiii!!.....reddy
# Hiii!!.....reddy