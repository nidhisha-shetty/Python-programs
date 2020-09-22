#Python doesnot support method overloading, however we may use other implementation in python to make the same function work differently i.e, as per the arguments.


#Example 1:
def sum(a,b):
	return a+b

def sum(a,b,c):
	return a+b+c

res=sum(2,3,5) #the function which is defined last will be considered
print(res)

#Example 2: 
class sum:
	def sum(self, a=None, b=None, c=None):  #takes 3 arguments
		if a!=None and b!=None and c!=None:
			return a+b+c
		elif a!=None and b!=None:
			return a+b
		else:
			return a

s1=sum()
print(s1.sum(2,3))		#passing two arguments(works)



