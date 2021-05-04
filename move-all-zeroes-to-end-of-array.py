# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. 

#Solution:
inp=[1, 2, 0, 0, 0, 3, 6]
count=0
for x in range(len(inp)):
    if inp[x]!=0:
        inp[x],inp[count]=inp[count],inp[x]
        count+=1

print(inp)

#Time complexity: O(n) 
#Space Complexity: O(1)
