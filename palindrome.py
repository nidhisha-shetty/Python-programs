#Check if a number is palindrome or not
number=523
temp=number
res=0
while(temp!=0):
    q=temp//10
    rem=temp%10
    res=res*10+rem
    temp=q
if res==number:
    print("The number is a palindrome")
else:
    print("The number is not a plaindrome")
