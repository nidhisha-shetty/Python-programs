a=list(input("Enter the first list"))
b=list(input("Enter the second list"))
a=[int(x) for x in a]
b=[int(x) for x in b]
for x in range(len(a)):
  print(a[x]+b[x])
