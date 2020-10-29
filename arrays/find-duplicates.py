#Find duplicates in an array

li=[2,2,1,5,4,5,7,5]
dup=[]
for x in li:
    res=li.count(x)
    if res>1:
        dup.append(x)
print(set(dup))
