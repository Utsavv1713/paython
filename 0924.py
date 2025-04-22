def str_length(s):
    if s == '':
        return 0
    return 1 + str_length(s[1:])

# Main
text = input("Enter a string: ")
print(f"Length of string: {str_length(text)}")
