#generaor reduces the effort of creating iter() and next(), this is achieved with the help of "yield" keyword 

def sum():

    n=1
    while(n<=10):
        sq=n*n
        yield sq
        n+=1
    
res=sum()
for i in res:
    print(i)