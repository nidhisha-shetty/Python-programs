# Take a two digit number from user as input and calculate their product and if the product is greater than 1000, print their sum

def prod_sum(int_1, int_2):

	while(int_1 in range(10,100) and int_2 in range(10,100)):
    	res=int_1*int_2
    	if res > 1000:
        	res=int_1+int_2
        	print("The sum is "+str(res))
        	break
    	print("The product is "+str(res))
    	break
	else:
    	print("Please enter two digit numbers")

int_1=int(input("Enter first number"))
int_2=int(input("Enter second number"))
prod_sum(int_1, int_2)