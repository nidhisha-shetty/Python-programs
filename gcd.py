import collections
def gcd(num_list):
    temp=[]
    for str_num in num_list:
        num=int(str_num)
        for x in range(1,num+1):
            if num%x==0:
                temp+=[str(x)]
    temp=collections.Counter(temp). #converts the list 'temp'  to dictionary having keys as the element of the list and values as the occurence of the elements in the list
    res=[item for item, count in temp.items() if count > len(num_list)-1]   #retrieving the keys with maximum values 
    return res[-1] #fetching the last key as the gcd
num_list=input("Enter numbers").split(' ')
print(gcd(num_list))