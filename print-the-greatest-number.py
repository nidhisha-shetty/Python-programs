#Take 3 numbers from user and print the greatest number 

a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if(a>b and a>c):
    print(tr(a) + "is greater")
elif(b>c and b>a):
    print(str(b) +"is greater")
else:
    print(str(c)+ "is greater")
