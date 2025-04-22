import random
rn = set()
for i in range(10):
    rn.add(random.randint(15,45))
print(rn)
c = 0
for i in rn:
    if i <30:
        c+=1
print(c)
s2 = set()
for i in rn:
    if i >35:
        s2.add(i)
print(s2)
        
        
