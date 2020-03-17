#1. lambda expressions are used in case we want to create functions without name i.e anonymous function, and contains only one expression.
#2. Instaed of creating a predefined function we can create a function when required using lamnda expression


#Example:

#normal function for adding two numbers:
def sum(a,b):
    return a+b
    
res=sum(2,3)
print(res)

#lambda expression for adding two nos:
res=lambda a,b: a+b
print(res(2,3))

