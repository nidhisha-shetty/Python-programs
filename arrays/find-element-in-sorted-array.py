#Find element in sorted array
def search_elem(arr, l, r, x):
    while l<r:
        mid=(l+r)//2
        if arr[mid]==x:
            return arr[mid]
        elif arr[mid]>x:
            r=mid-1
        elif arr[mid]<x:
            l=mid+1

arr=[2,5,6,8]
x=6
l=0
r=len(arr)-1
search_elem(arr, l, r, x)
