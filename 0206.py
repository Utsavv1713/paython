def dig():
    x=float(input("enter the number between 0 to 10000"))
    if(x>=0 and x<10):
        print("single digit")
    elif(x>=10 and x<100):
        print("double digit")
    elif(x>=100 and x<1000):
        print("three digit")
    elif(x>=1000 and x<10000):
        print(" four digit")
    elif(x==10000):
        print("five digit")
    else:
        print("not a valid number")
     
dig()    
