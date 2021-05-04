# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. 

#Solution:
def push_zero_to_end(inp):
    count=0
    for x in range(len(inp)):
        if inp[x]!=0:
            inp[x],inp[count]=inp[count],inp[x]
            count+=1

inp=[1, 2, 0, 0, 0, 3, 6]
print(push_zero_to_end(inp))

#Time complexity: O(n) 
#Space Complexity: O(1)
