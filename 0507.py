stack = []
def push():
    n = int(input("enter element to push:"))
    stack.append(n)
print(stack)

def pop():
    if not stack:
        print("empty")
    else:
        r = stack.pop()
        print(r)
        
