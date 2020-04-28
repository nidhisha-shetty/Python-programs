li=[1,2,3,4,5]

for x in li:  #calls __iter__() and __next__() function internally; __iter__() calls the list(li) object and __next__() calls the objects in list(li) one by one. 
	print(x)


#In the above code, list is the iterator which calls iter() and next() methods internally , in the following code we will create our own iterator and call iter() and next() method in the program itself.
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


#Reference: (https://www.geeksforgeeks.org/iterators-in-python/)
# Iterator in python is any python type that can be used with a ‘for in loop’. Python lists, tuples, dicts and sets are all examples of inbuilt iterators. These types are iterators because they implement following methods. In fact, any object that wants to be an iterator must implement following methods.

#     __iter__ method that is called on initialization of an iterator. This should return an object that has a next or __next__ (in Python 3) method.
#     next ( __next__ in Python 3) The iterator next method should return the next value for the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() on the iterator object. This method should raise a StopIteration to signal the end of the iteration.
