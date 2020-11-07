#8. Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#Solution
arr=[9,1,3,2,5,6,7,8,4]
sum=0
for x in range(len(arr)-1):
    if arr[x]+1==arr[x+1]:
        sum+=1
print(sum)
