#Check if a number is palindrome or not
num=565
res=0
q=num
while(q!=0):
	new_q=q//10
	rem=q%10
	res=res*10+rem
if res==num:
	print("The number is a palindrome")
else:
	print("The number is not a plaindrome")
