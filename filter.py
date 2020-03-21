#filter() is used to filter elements from a list based on some condition


#filter function in predefined function
def greater_than_five(n):
	return n>5
num = [1,2,3,4,5,6,7,8,9,10]
res=list(filter(greater_than_five, num))
print(res)


#filter function in lambda function
num = [1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x:x>5, num))
print(res)



