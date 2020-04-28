#Example:
li=[1,2,3,4,5]

for x in li:  #calls __iter__() and __next__() function internally; __iter__() calls the list(li) object and __next__() calls the objects in list(li) one by one. 
	print(x)


#In the above code, list is the iterator which calls iter() and next() methods internally , in the following code will create our own iterator and call iter() and next() method in the program itself.
#Creating our own iterator(using __iter__() and __next__() function)

class iteration:

	def __init__(self, number):
		self.num= number

	def __iter__(self):
		return self

	def __next__(self):
		if self.num<=10:
			val=self.num
			self.num+=1
			return val
		else:
			raise StopIteration
	
it=iteration(1)

for i in it:
	print(i)


