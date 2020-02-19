In order to avoid coding same set of steps repeatedly, we use functions.
for example, if we have payment option thrice in our project, we will create the paymant function once, and just call it thrice, hence avoiding repeated codes.



def sum(num1, num2):            #defining sum function
    add=num1+num2
    return(add)

res1=sum(3,4)                   #calling sum function
print(res1)

res2=sum(7,10)                  #calling sum function
print(res2)

res3=sum(2,6)                   #calling sum function
print(res3)



In the example we are asking the function to just return the value and not print it. We are printing the result on function call.

Inversely we can also ask the function to print the value, and not print the result on function call.

def sum(num1, num2):
    add=num1+num2
    print(add)

sum(3,4)


sum(7,10)


sum(2,6)
