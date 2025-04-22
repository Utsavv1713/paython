def convert(s):
    words = set(s.split())
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

# Test
print(convert("red blue green red yellow blue"))
