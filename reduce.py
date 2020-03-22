#reduce() performs a particular function on all the elements together in the list and returns a single value
#reduce() is defined in functools, hence we need to import functools at the start(** import functools **)


#reduce function with predefined function
def reduce(a,b):
    return a+b
num=[1,2,3,4,5,6,7,8,9]
res=list(reduce(reduce, num))
print(res)


#reduce function with lambda expression
num=[1,2,3,4,5,6,7,8,9]
res=int(reduce(lambda a,b:a+b, num))
print(res)
