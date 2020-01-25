#using sort() method
li=[1,5,0,9,2,3]
li.sort()
print(li[-1])

#using for loop and if condition
li=[1,5,0,9,2,3]
x=li[0]
for y in li:
  if y > x:
    x=y
print(x)


