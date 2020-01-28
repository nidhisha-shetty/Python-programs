total=0
li=list(input("Enter a list of numbers"))
li_1=[int(elem) for elem in li]
for index in range(len(li_1)):
  total=total+li_1[index]
print("Sum of elements in list is: "+str(total))
