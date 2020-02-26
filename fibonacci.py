##Fibonacci series:0 1 1 2 3 5 8 13 21

Example 1: 
n=int(input("Enter a number"))
print("0")
print("1")
res1=0
res2=1
for x in range(n-2): // 'n-2', since 0 and 1 is already being printed at the start 
    temp=res1+res2
    print(temp)
    res1=res2
    res2=temp

    
Example 2: Executing the series till the user input and checking if the input is greater than 0
n=int(input("Enter a number"))
if n>0:
    print("0")
    print("1")
    res1=0
    res2=1
    for x in range(n-2):
        temp=res1+res2
        print(temp)
        res1=res2
        res2=temp
        
   
Example 3: Printing fibonacci series till user input.
n=int(input("Enter a number"))
print("0")
print("1")
res1=0
res2=1
for x in range(10):
    temp=res1+res2
    if temp<n:
        print(temp)
        res1=res2
        res2=temp
    
