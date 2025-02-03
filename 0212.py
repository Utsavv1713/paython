radius=float(input("enter the radius."))
x=float(input("enter the first coordinets"))
y=float(input("enter the second coordinets"))

a=pow(x,2)
b=pow(y,2)

c=a+b
d=pow(c,1/2)

if(d==radius):
    print("equle to radius")
elif(d>radius):
    print("outside radius")
else:
    print("inside the radius")