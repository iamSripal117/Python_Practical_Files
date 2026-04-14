def testing(): # called to display
    print("In testing fn")
    print("Last line of testing fn")
    
def display():  # calling to testing and called to show 
    print("In display fn")
    print("2nd line of display fn")
    print("Last line of display fn")
    testing()
    print("return to display")

def show(): # calling function 
    print("In show fn")
    print("2nd line of show fn")
    print("Last line of show fn")
    display()
    print("Return to show")

show()
