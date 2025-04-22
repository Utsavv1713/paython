import math
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def sin(x,terms=10):
    sinx=0
    for n in range(terms):
        terms = ((-1)**n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sinx += terms
    return sinx

s = float (input("enter the value of x :"))
print(sin(s)) 
