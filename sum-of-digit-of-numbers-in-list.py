li=[123,456,32,56]

for num in li:
    total=0
    for digit in str(num):
        
        total=total+int(digit)
    print(total)
##result: 6,15, 5, 11

li=[123,456,32,56]
total=0
for num in li:
    
    for digit in str(num):
        
        total=total+int(digit)
    print(total)
###result: 37

