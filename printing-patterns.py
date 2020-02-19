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

str1='efgh'
str2='ijk'
for num in range(4):
    print(str1[:num+1]+str2[num:])
    
o/p:    eijk
        efjk
        efgk
        efgh

str1='0123456789'
str2='9876543210'
for x in range(10):
    print(str1[:x+1]+str2[x:])
    
o/p: 09876543210
     01876543210
     01276543210
     01236543210
     01234543210
     01234543210
     01234563210
     01234567210
     01234567810
     01234567890
        
for out in range(10):
    for inn in range(0, out+1):
        print(inn+1,end="")
    print()
for out in reversed(range(10)):
    for inn in range(0, out):
        print(inn+1,end="")
    print()
    
o/p:
1
12
123
1234
12345
123456
1234567
12345678
123456789
12345678910
123456789
12345678
1234567
123456
12345
1234
123
12
1

