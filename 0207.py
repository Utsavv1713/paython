def leapyear():
    x=float(input("enter the year"))
    
    if(x%400==0):
        print(x," is not leap year")
    elif(x%4==0):
        print(x," is leap year")
    else:
        print(x," is not a leap year")
        
leapyear()

