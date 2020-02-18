for x in range(4):
    for j in range(4):
        print('#', end='')
    print()
    
o/p: ####
     ####
     ####
     ####

for x in range(4):
    for j in range(x+1):
        print('#', end='')
    print()
    
o/p: #
     ##
     ###
     ####
    
for x in range(4):
    for j in range(4-x):
        print('#', end='')
    print()
   
o/p: ####
     ###
     ##
     #

for out in range(4):
    for inn in range(0, out+1):
        print(inn+1,end="")
    print()
   
o/p:    1
        12
        123
        1234
        
for x in range(4):
    for y in range(x,4):
        print(y+1,end="")
    print() 
    
o/p:    1234
        234
        34
        4   
