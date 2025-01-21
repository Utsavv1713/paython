def validtringle():
    x=float(input("enter the 1st angle: "))
    y=float(input("enter the 2nd angle: "))
    z=float(input("enter the 3rd angle: "))

    if((x+y+z)==180):
        print(" valid tringle ")
    else:
        print(" not a valid tringle ")
validtringle()
