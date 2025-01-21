def ls3():
 x=float(input("enter the number"))
 y=float(input("enter the number"))
 z=float(input("enter the number"))
 
 large=x
 if y>large:
    large=y
 if z>large:
    large=z

 small=x
 if small<y:
    small=y
 if small>z:
    small=z

 if large==small:
     print("all the value are same")
 else:
     print(large," is largest","&",small," is smallest")
 
ls3()
    
