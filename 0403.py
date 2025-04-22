def count_alph_digits(s):
    alph = digits = 0
    for char in s:
        if char.isalpha():
            alph+=1
        elif char.isdigit():
            digits+=1

    return alph,digits

string = input("enter a string:")
alph,digits = count_alph_digits(string)
print("no. of alphabets:",alph)
print("no. of digits:",digits)
