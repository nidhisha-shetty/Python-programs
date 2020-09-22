def mul(num):
    if num==1:
        return 1
    else: 
        num=num*mul(num-1)
        return num



num=int(input("Enter a number: "))
res=mul(num)
print(res)
