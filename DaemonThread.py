# These threads works in background

# example 1
from threading import *

print("Hello......")
print(current_thread().name)
print(current_thread().daemon)

#current_thread() is main thread

