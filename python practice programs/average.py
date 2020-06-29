#calculate the average of numbers given in a list, and print the result upto 2 decimals

def avg(li):
    count=0
    total=0
    for x in n:
        total+=int(x)
    for y in n:
        count+=1
    result=total/count
    return result
n=list(input("Enter a list of numbers").split(' '))
print("%.2f" % avg(n))