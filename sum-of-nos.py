#Find the sum of numbers in a list using for loop
x=[1,2,3]
sum=0
for z in x:
    sum+=z
print(sum)


#Find the sum of numbers in a list using for while loop
x=[1,2,3]
sum=0
loop=0
print(len(x))
while (loop < len(x)):
    sum+=x[loop]
    loop+=1
print(sum)


#Find the sum of numbers in a list using recurssion
def sum(x):
    if len(x)==1:
        return x[0]
    else:
        return x[0]+sum(x[1:])
    

x=[1,2,3,4,5]
res=sum(x)
print(res)
