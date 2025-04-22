d1 = {'fruits':50,'vegetables':67,'bread':24,'statitems':45}
d2 = {'fruits':5,'vegetables':7,'bread':4,'statitems':8}
tb = 0
for i,q in d2.items():
    if i in d1:
        tb += d1[i] * q
print(tb)
    
