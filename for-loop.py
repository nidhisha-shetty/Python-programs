#printing elements in reverse order using for loop
for x in range(20,10,-1):
    print(x)

#printing even numbers from 0-100
for x in range(0,101,2):
    print(x)
   
#printing odd numbers from 0-100
for x in range(1,100,2):
    print(x)
    
#printing elements of a list in reverse order
a=[1,2,3]
for x in a[::-1]:
    print(x)

#printing elements of a list in sequence    
a=[1,'abc',2,'pqr']
for x in a:
    print(x)
