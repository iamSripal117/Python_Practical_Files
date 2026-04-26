def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
def inp_data():
    n=int(input("Enter thr n value"))
    x=fib(n)
    print("Series is:",x)
    
inp_data()

