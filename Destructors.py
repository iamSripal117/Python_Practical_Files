##Synatax for destructors

##def__del__(self):
##    statements


##Example-1:

class Demo:
    def __init__(self):
        print("Constructors")
    def __del__(self):
        print("Destructors")
##    def show(self):
##            print("In show")
##            print("Last of show")
d = Demo()
d2 = Demo()
##d.show()


##Destructors will nor print all the time only may get delay to print
##Python does not guarantee immediate destructor execution
