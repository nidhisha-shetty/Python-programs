li1=list(input("Enter a list of numbers"))
li2=list(input("Enter a list of numbers"))
li3=[]
for x in li1:
    if int(x)%2!=0:
        li3+=x
        
for y in li2:
    if int(y)%2==0:
        li3+=y
print(li3)