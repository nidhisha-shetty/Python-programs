#method 1:
z=5
for x in range(z):
    for y in range(z,0,-1):
        print('*', end="")
    z=z-1
    print('\n')

#method 2:
for x in range(6,0,-1):
    for y in range(x-1,0,-1):
        print('*',end=' ')
    print('\n')
    
#output:
* * * * * 

* * * * 

* * * 

* * 

*
