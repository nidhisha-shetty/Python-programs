#using inbuilt functions
def missingelems(li):
    miss=[]
    for y in range(min(li), max(li)+1):
        if y not in li:
            miss.append(y)
    return miss
li=[2, 5, 1, 4,7,10,15]
missingelems(li)

#without using inbuilt functions
def missingelems(li):
    miss=[]
    min_val = max_val=li[0]
    for min_x in li:
        if min_x < min_val:
            min_val=min_x
    for max_x in li:
        if max_x > max_val:
            max_val = max_x
    for y in range(min_val, max_val):
        if y not in li:
            miss.append(y)
    return miss
li=[2, 5, 1, 4,7,10,15]
missingelems(li)
