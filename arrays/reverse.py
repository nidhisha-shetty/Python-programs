li=[1,2,3,4,5,6]
x=0
y=-1
while (x<len(li)//2):
    li[x]=li[x]+li[y]
    li[y]=li[x]-li[y]
    li[x]=li[x]-li[y]
    x+=1
    y+=-1
print(li)
