def sum(num):
    temp=num
    if temp==0:
        return 0
    else:
        sum_temp=int(temp)+int(sum(int(temp)-1))
        return sum_temp



num=input("Enter a number")
res=sum(num)
print(res)