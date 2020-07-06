#Problem statement: Print the following pattern
1
22
333
4444
55555


#Solution:
for x in range(1,6):
    for y in range(x):
        print(x, end='')
    print()