def frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

# Test
print(frequency("the cat sat on the mat with the cat"))
