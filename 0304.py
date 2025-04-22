def strtolowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <='Z':
            result+= chr(ord(char)+32)
        else:
            result+=char
    return result

userinput= input("enter a string:")
print("lowercase:",strtolowercase(userinput))
def strtouppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <='z':
            result+= chr(ord(char)-32)
        else:
            result+=char
    return result

print("uppercase:",strtouppercase(userinput))

def togglecase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result+=chr(ord(char)+32)
        elif 'a' <= char <='b':
            result+=chr(ord(char)-32)
        else:
            result+=""

    return result

print("togglecase:",togglecase(userinput))
