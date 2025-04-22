import random
l1 = []
for i in range(50):
    l1.append(random.randint(1,30))
print(l1)

new = []
for i in l1:
    if i not in new:
        new.append(i)
print(new)
