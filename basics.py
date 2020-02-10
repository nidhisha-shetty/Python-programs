#taking input from users for adding two numbers

a=int(input("Enter the first number"))
b=int(input("Enter the second numebr"))
sum=a+b
print(sum)

#taking a single character from user as input
ch=input("Enter a character")[0]
print(ch)

#taking user input while executing file from command prompt
import sys
a=int(sys.argv[1])  #taking index number as 1 and not 0 because 0 is the index number for file name (example: python file_name.py 2 3). 
b=int(sys.argv[2]) 
print(a+b)


#using 'eval' function (evaluates the expression given as input)
res=eval(input("Enter a mathematical expression"))
print(res)

