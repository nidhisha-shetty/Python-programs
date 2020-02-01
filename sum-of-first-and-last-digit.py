#sum of first and last digit of a number

num=list(input("Enter a number"))
num_int=list(int(x) for x in num)
print(num_int[0]+num_int[-1])



#sum of first and last digit of the numbers in list
li_1=list(input("Enter the list").split())
for num in li_1:
 	li_2=list(int(digit)for digit in num)
 	print("The sum of first and last digit of "+str(num)+" is: "+str(li_2[0]+li_2[-1]))
