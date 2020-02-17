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
