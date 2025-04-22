def ispalindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

# Test
print(ispalindrome("A man a plan a canal Panama"))  # True
print(ispalindrome("Hello"))  # False
