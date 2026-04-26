##A method is created inside another method

##Example 1

class Demo:
    def show(self):
        self.x= 10
        print("Show method")

        def display(): # this nested method is created inside show method doesn't have access to self.x
            print("display method")
            print(self.x)
        display()
d =Demo()
d.show()

