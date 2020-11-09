# 7. How do you search a target value in a rotated array?

arr=[15,18,2,5,6,8]
target=8
min=0
for x in range(len(arr)):
    if arr[x]<arr[min]:
        min=x                  
def bs(l,r):
    mid=(l+r)//2
    if arr[mid]==target:
        return mid
    if arr[0]<target:
        bs(0,mid-1)
    if arr[0]>target:
        bs(mid+1,len(arr)-1)
bs(0,len(arr)-1)    
