##Synatx
##for variable in range(...):
##    statements

##[else:
## statements]in python syntax if we write the code in square brackets that is meant to be optional



##Example1

##for i in range(5):
####    print(i)
##    print(i,end=" ")
####0,1,2,3,4    
##    
##
##
##for i in range(10,15):
##    print(i,end=" ")
####10,11,12,13,14


##for i in range(1,10,2):
##    print(i,end=" ")
####1,3,5,7,9    


##for i in range(2,10,2):
##    print(i,end=" ")
####2,4,6,8    

##
##for i in range(10,1,-2):
##    print(i,end=" ")
##10,8,6,4,2    


##for i in range(10,0,-2):
##    print(i,end=" ")
##
##10,8,6,4,2





####Example-2
####WAP to input n value.Display sum of n natural numbers.
##
##n=int(input("Enter the value:"))
##
##s=0
##
##for i in range(1,n+1):
##    s=s+i
##    print(i)
##else:
##    print("Sum is :",s)

####Exmaple-3
####WAP to input n value.Display Mathematical table of that number
##n=int(input("Enter the value:"))
##
##for i in range(1,11):
##    print(n,"*",i,"=",n*i)


##Example-4
##WAP to input n value.Display factors of the given number?
##
##n=int(input("Enter the value:"))
##
##for i in range(1,n+1):
##    if n%i==0:
##        print(i,"*",int(n/i),'=',n)

        
##Example-5

####WAP to input n value.Check whether a given number is perfect number or not?
##
##n = int(input("Enter the number: "))
##
##s = 0
##
##for i in range(1, n):
##    if n % i == 0:
##        s = s + i
##
##if s == n:
##    print(n, "is a Perfect Number")
##else:
##    print(n, "is not a Perfect Number")
##            
            

##Prime NUmber
##n = int(input("Enter the number: "))
##
##for i in range (2,n-1):
##    if n%i==0:
##        print(f"{n} is not a prime number")
##        break
##else:
##    print(f"{n} is a prime number")


n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "is", fact)


































    
