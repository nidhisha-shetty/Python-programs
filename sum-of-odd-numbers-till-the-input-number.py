#sum of all odd numbers till n

num= int(input("Enter a number"))
sum=0
for x in range(1,num):
	if x%2!=0:
		sum+=x
print("The sum of all odd numbers till " + str(num) + " is "+str(sum))
