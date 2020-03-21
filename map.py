#map() performs a particular operation on all the elements in the list and returns them

#map function with predefined function
def mapping(n):
    return n*2
num=[1,2,3,4,5,6,7,8,9]
res=list(map(mapping, num))
print(res)


#map function with lambda expression
num=[1,2,3,4,5,6,7,8,9]
res=list(map(lambda x:x*2, num))
print(res)