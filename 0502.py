import random
l1 = []
for i in range(20):
    l1.append(random.randint(1,100))
print(l1)

n = int(input("enter a number:"))
position = []
for i in range(len(l1)):
        if l1[i] == n:
            position.append(i)

if position:
        print(position)
else:
    print("not found")


