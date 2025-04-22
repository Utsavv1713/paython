def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

n = int(input("enter a number:"))
print(factorial(n))
