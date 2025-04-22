import random
l1 = []
for i in range(30):
    l1.append(random.randrange(-100,100))
print(l1)

l2 = []
for num in l1:
    if num < 0:
        l2.append(num)
print(l2)
l3 = []
for num in l1:
    if num >= 0:
        l3.append(num)
print(l3)
