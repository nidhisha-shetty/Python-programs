inp = input("Enter a number")
rev=inp[::-1]
print(rev)
if inp == rev:
    print("The numbers are same")
else:
    print("The numbers are not same")