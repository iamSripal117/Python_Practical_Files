##Example:1 calling and called functions

##def testing(): # called to display
##    print("In testing fn")
##    print("Last line of testing fn")
##    
##def display():  # calling to testing and called to show 
##    print("In display fn")
##    print("2nd line of display fn")
##    print("Last line of display fn")
##    testing()
##    print("return to display")
##
##def show(): # calling function 
##    print("In show fn")
##    print("2nd line of show fn")
##    print("Last line of show fn")
##    display()
##    print("Return to show")
##
##show()







##Example:2 WAP to input 2 values using user defined functions
##def display(a, b, c):
##    print("Sum of",a,"and",b,"is",c)
##
##def calc(x, y):
##    z=x+y
##    display(x, y, z)
##
##def inp_data():
##    a=int(input("Enter a value : "))
##    b=int(input("Enter b value : "))
##    calc(a, b)
##
##inp_data()



##Example 3: Write a program to input n value thru one function and display mathematical table of that number thru another function?

##def math_tab(x):
##    for i in range(1, 11):
##        print(x,'*',i,'=',x*i)
##
##def inp_data():
##    n=int(input("Enter n value : "))
##    math_tab(n)
##
##inp_data()

##normal for loop process for printing the table of any number
##n=int(input("Enter the n value:"))
##for i in range(1, 11):
##        print(n,'*',i,'=',n*i)





##************************Return Keyword**********************

##Example 4:using Return keyword returning only one reference

##def calc(x, y): # called function
##    z=x+y
##    return z
##
##    
##def inp_data(): # calling function
##    a=int(input("Enter a value : "))
##    b=int(input("Enter b value : "))
##    res=calc(a, b)			
##    print("Sum is",res)
##
##inp_data()



##Example 5: returning more then one references


##def calc(x, y): # called function
##    s=x+y
##    d=x-y
##    p=x*y
##    q=x/y
##    r=x%y
##    return s, d, p, q, r
##
##    
##def inp_data(): # calling function
##    a=int(input("Enter a value : "))
##    b=int(input("Enter b value : "))
##    r1, r2, r3, r4, r5=calc(a, b)
##    print("Sum is",r1)
##    print("Diff is",r2)
##    print("Product is",r3)
##    print("Quotient is",r4)
##    print("Remainder is",r5)
##    
##inp_data()


##      (OR)

##def calc(x, y): # called function
##    s=x+y
##    d=x-y
##    p=x*y
##    q=x/y
##    r=x%y
##    return s, d, p, q, r
##
##    
##def inp_data(): # calling function
##    a=int(input("Enter a value : "))
##    b=int(input("Enter b value : "))
##    res=calc(a, b)				
##    print(type(res))
##    print(res)
##    for obj in res:
##        print(obj)
##
##        
##inp_data()













								  	














































