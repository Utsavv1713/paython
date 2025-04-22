s = input("enter a string:")
cf = {}

for char in s:
    if char in cf:
        cf[char] += 1
    else:
        cf[char] = 1
print(cf)
        
        
