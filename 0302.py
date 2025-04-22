def remove_substring(onestring,removestring):
    return onestring.replace(removestring,"")
onestring = "abcdef"
removestring = "cd"
finalstring=remove_substring(onestring,removestring)
print(finalstring)

