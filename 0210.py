l=int(input("enter a number:"))
b=int(input("enter a number:"))

area=l*b
paramiter=2*(l+b)

if(area>paramiter):
    print("area>paramiter")
elif(area==paramiter):
    print("area=paramiter")
else:
    print("area<paramiter")