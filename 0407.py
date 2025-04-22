#code to write factoral
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

#code to write nCr and nPr
def ncr_npr(n,r):
    if n<r:
        print("invalid input ")
        return
    nfact = factorial(n)
    rfact = factorial(r)
    nrfact = factorial(n-r)

    ncr = nfact // (rfact * nrfact)
    npr = nfact // (nrfact)

    print(n,"C",r,"=", ncr)
    print(n,"P",r,"=", npr)

ncr_npr(10,8)
