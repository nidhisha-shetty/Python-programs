#Finding factorial of a number using recurssion(calling the same function again and again)

def fact(n):
    if n==0:
        return 1
    res=n * fact(n-1)
    return res

fact(5)
