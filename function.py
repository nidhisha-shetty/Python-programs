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

def sum(num1, num2):  #passing formal arguments
    add=num1+num2
    print(add)

sum(3,4)              #passing actual arguments


sum(7,10)             #passing actual arguments


sum(2,6)              #passing actual arguments

                      
    
    
    
    
                                                #Types of argument
#formal arguments
#actual arguments
    #position
    #keyword
    #default
    #variable length
       
        
        
#Position arguments:
ex1:
def person(name, age):
    print(name)
    print(age)

person('nidhisha', 25)              #actual arguments position should be relative to formal arguments position

ex2: 
def person(name, age):
    print(name)
    print(age-5)

person(25, 'nidhisha') 
#the preceding code block will throw an error since 5 cannot be subtracted from a string('nidhisha'), hence position arguments are required, 
#incase we donot know the actual sequence, we can use keyword arguments as shown below

#keyword arguments:
def person(name, age):
    print(name)
    print(age)

person(age=25, name='nidhisha')     #age and name are keywords, incase we do not know the sequence of formal arguments   
        
    
#default:
ex1:
def person(name, age=18):  #default argument is taken as 18, incase the age is not provided during function call
    print(name)
    print(age)

person('nidhisha')


ex2:
    
def person(name, age=18):  #default argument is taken as 18, incase the age is not provided during function call
    print(name)
    print(age)

person('nidhisha', 25) #25 will overwrite 18 in this case



#Variable length argument

def sum(num1, *num2):            #num2 will accept multiple arguments i.e from 2,3,4, hence forming a tuple
    
    temp=num1
    for num in num2:
        temp=temp+num
    print(temp)

sum(1,2,3,4)





















