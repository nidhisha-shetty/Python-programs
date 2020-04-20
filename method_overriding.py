#Example 1, with output "Method A"

class A:
	
	def show(self):
		print("Method A")
		
class B(A):
	
	pass

b1=B()
b1.show()


#Example 2, with output "Method B
class A:

	def show(self):
		print("Method A")

class B(A):

	def show(self):     		 #method overriding (show() of class B overrides show() method of class A)
		print("Method B")

a1=B()
a1.show()
