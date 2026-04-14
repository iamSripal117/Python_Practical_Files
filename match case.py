
'''(for int)
a=int(input("Enter the choice="))

match a:
    case 1:
        print("choice entered is 1")
    case 2:
        print("choice entered is 2")
    case _:
        print("invalid choice")'''


'''(for float)

a=float(input("Enter the choice="))

match a:
    case 1.6:
        print("choice entered is 1.6")
    case 2.7:
        print("choice entered is 2.7")
    case _:
        print("invalid choice")'''

'''(for str)

a=str(input("Enter the choice="))

match a:
    case 'a':
        print("choice entered is a")
##(you can add int to the strings also)
    case '2': 
        print("choice entered is 2")
    case _:
        print("invalid choice")'''


##for Days like mondays,tuesdays........

R=input("Enter the choice=")

match R:
    case "Mon" | "Tue" | "Wed" | "Thurs" | "Fri":
        print("Weekday")
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("invalid choice")
















        
        
