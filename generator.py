#generator reduces the effort of creating iter() and next() as in iterators, this is achieved with the help of "yield" keyword 

#Example:
def sum():

    n=1
    while(n<=10):
        sq=n*n
        yield sq
        n+=1
    
res=sum()
for i in res:
    print(i)
