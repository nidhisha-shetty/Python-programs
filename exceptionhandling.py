# Exception handling is user defined errors/exceptions 

#Example 1:

num1=5
num2=3

try:
	print(num1/num2)

except Exception as e:
	print("Number cannot be divided by 0")

finally:
	print("Happy Coding")


# Example 2:
num1=5
num2=2

try:
    print(num1/num2)
    inp=int(input("Enter a number"))
    print(inp)

except ZeroDivisionError as n:						#Handles zerodivision exception(number divided by 0)
    print("Number cannot be divided by 0", n)    

except ValueError as ve:							   #Handles incorrect input(input of different data type)
    print("Please enter a number", ve)

except Exception as e:								#Handles all other errors
	print("Incorrect input")

finally:
    print("Happy learning!")