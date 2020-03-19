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

##Mathematical operations using lambda
cube=lambda x: x*x*x
print(cube(3))

square=lambda x: x*x
print(square(3))

addition=lambda x,y:x+y
print(addition(2,3))


subtraction = lambda x,y: x-y
print(subtraction(3,2))

multiplication = lambda x,y:x*y
print(multiplication(3,4))

division= lambda x,y: x//y
print(division(4,2))
