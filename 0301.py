def countvowel():
    str1= input(str("enter a string:"))
    vowels = "aeiouAEIOU"
    i=0
    for char in str1:
        if char in vowels:
            i+=1
    print(i)

countvowel()
