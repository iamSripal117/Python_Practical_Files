class B1:
    def show(self):
        print("B1 show method")
class D1(B1):
    def show(self):
        super().show()
        print("D1 show method")

class D2(D1):
    def show(self):
        super().show()
        print("D2 show method")
print(D2.__base__) #D1
print(D1.__base__) #B1
print(B1.__base__) #object
d = D2()  #creating instance for class D2
d.show() #calling show method using instance
        