x1=int(input("enter a number:"))
y1=int(input("enter a number:"))
x2=int(input("enter a number:"))
y2=int(input("enter a number:"))
x3=int(input("enter a number:"))
y3=int(input("enter a number:"))

if((y2-y1)/(x2-x1)==(y3-y2)/(x3-x2)==(y1-y3)/(x1-x3)):
    print("all points are in one line.")
else:
    print("this is in different dimension")