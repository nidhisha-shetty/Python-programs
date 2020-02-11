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

                                                          
  
                                                        #LISTS
#list of int type
li_num=[1,5,7,9,13,15] 

#retrieving the 13 from the list
li_num[4] or li_num[-2]

#retrieving all the elements from the list
lin_num[:]  

#retrieving all the elements in reverse order from the list
li_num[::-1]

#list of string type
li_str=['abc','pqr','xyz']

#retrieving 'pqr' from li_str
li_str[1]

#creating nested list
data=[li_num, li_str]







