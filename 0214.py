m1=int(input("enter teh first suubject marks"))
m2=int(input("enter teh second suubject marks"))
m3=int(input("enter teh third suubject marks"))

marks=(m1+m2+m3)/3

if(marks<0 or marks>100):
    print("invalid marks")
elif(marks>0 and marks<=39):
    print("grade F")
elif(marks>39 and marks<=44):
    print("grade P")
elif(marks>44 and marks<=49):
    print("grade C")
elif(marks>49 and marks<=54):
    print("grade B")
elif(marks>54 and marks<=59):
    print("grade B+")
elif(marks>59 and marks<=69):
    print("grade A")
elif(marks>69 and marks<=79):
    print("grade A+")
else:
    print("grade O")