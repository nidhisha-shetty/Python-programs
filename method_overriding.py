class A:
	def show(self):
		print("Method A")
class B(A):
	pass
b1=B()
b1.show()



# class A:
# 	def show(self):
# 		print("Method A")
# class B(A):
# 	def show(self):     	 #method overriding (show() of class B overrides show() method of A)
# 		print("Method B")
# a1=B()
# a1.show()