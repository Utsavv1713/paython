s1 = {"ansh","brook","aman","amanadiel","bipin"}
s2 = set()
s3 = set()
for i in s1:
    if i.startswith("a"):
        s2.add(i)
    elif i.startswith("b"):
        s3.add(i)
print(s2,s3)
