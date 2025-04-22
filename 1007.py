remove_words = {"a", "an", "the"}

with open("input_text.txt", "r") as infile, open("cleaned_text.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        filtered = [word for word in words if word.lower() not in remove_words]
        outfile.write(" ".join(filtered) + "\n")

print("Filtered file created as cleaned_text.txt")
