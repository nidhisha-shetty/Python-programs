def sort_list(li):
    li.sort()
    return li

li=list(input("Enter a list of numbers: ").split(" "))
res=sort_list(li)
print(res)
