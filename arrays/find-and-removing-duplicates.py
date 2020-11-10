#Find duplicates in an array
li=[2,2,1,5,4,5,7,5]
dup=[]
for x in li:
    res=li.count(x)
    if res>1:
        dup.append(x)
print(set(dup))

#Removing duplicates
def remove_duplicate(li):
    x=0
    while x<(len(li)-1):
        if li[x]==li[x+1]:
            li.remove(li[x+1])
        x+=1
    return li
li=[1,1,2,2,3,4,5]
print(remove_duplicate(li))
