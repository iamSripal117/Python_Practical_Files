'''Example 1
x=1
while x<=5:
    print(x)
    x=x+1'''

####Example1:WAP to input n value.Display first n odd numbers
##
##n=int(input("Enter n value:"))
##x=1
##while x<=n*2:
##    print(x)
##    x+=2


####Example2:WAP to input n value.Display first n even numbers
##
##n=int(input("Enter n value:"))
##x=2
##while x<=n*2:
##    print(x)
##    x=x+2    


####Exanple6:WAP to check whether a given number is prime number or not?
##
##n=int(input("Enter n value:"))
##x=2
##while x<n:
##    if n%x==0:
##        print(f"{n}is not a prime number")
##        break
##
##    x=x+1
##if x==n:
##    print(f"{n} is a prime number")



##start=int(input("Enter the range:"))
##end=int(input("Enter the range:"))
##while start<=end:
##    x=2
##    while x<start:
##        if start%x==0:
##            break
##        x+=1
##    if x==start:
##        print(f"{start}is a prime number")
##        start+=1      


n=int(input("Enter the n value:"))
t=n
s=0

while t>0:
    r=t%10
    s=s+r
    t=int(t/10)
print(f"sum of digits of {n} is {s}")    












































    
    
