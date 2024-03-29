'''
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
Example:
arr = [1,1,2,2,3]
'''
arr = [-1, 2, 3, 4, 4, 6, 6, -1, -1, 2]
di = {}
for x in arr:
    if x in di.keys():
        di[x]+=1
    else:
        di[x]=1
values = list(di.values())
max_value = max(values) 
res = []
for key in di.keys():
    if di[key] == max_value:
        res.append(key)
print(min(res))
