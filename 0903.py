import random
l = []
for i in range(10):
    l.append(random.randint(-15,15))
print(l)

l2 = list(map(lambda x:x**2,l))
print(l2)
