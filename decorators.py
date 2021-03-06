#Decorators are used to add more features to an already existing function without modifying it

#Example 1: If divisor is greater than dividend, then reverse the numbers and then divide
def  div(a,b):
    print(a/b)

def smart_div(func):                    #defining decorator
    def smart_div_args(x,y):
        
        if x<y:
            x,y = y,x
        return func(x,y)
    return smart_div_args
    
division=smart_div(div)                #calling decorator    #similar to @smart_div
division(4,8)

#Example 2: Multiplication of numbers, if either of the two numbers is equal to zero, print an error message, else return the result

def dec(function):                   #defining decorator
    def function_args(x,y):
        if x<=0 or y<=0:
            print("Please enter numbers greater than 0")
            return
        function(x,y)
    return function_args
@dec                                  #calling decorator      #similar to mul=dec(mul)
def mul(a,b):
    print(a*b)
value1 = int(input("Enter first number"))
value2 = int(input("Enter second number"))
mul(value1, value2)

#Example 3:
import time
def time_dec(func):
    def time_dec_args(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        stop=time.time()
        print("time taken"+str(start-stop))
        return result
    return time_dec_args

@time_dec
def cube(num):
    res=num*num*num
    return res
    
print(cube(3))

