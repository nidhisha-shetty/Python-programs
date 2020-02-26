print("0")
print("1")
res1=0
res2=1
for x in range(10):
    temp=res1+res2
    print(temp)
    res1=res2
    res2=temp
