						#single level inheritance
class A:
	def feature1(self):
		print("feature 1 of A")
	def feature2(self):
 		print("feature 2 of A")

class B(A):
	pass

a1=A()
b1=B()
b1.feature1()	



						#multi level inheritence
class A:
	def feature1(self):
		print("feature 1 of A")
	def feature2(self):
 		print("feature 2 of A")

class B(A):
	pass

class C(B):
	pass

a1=A()
b1=B()
c1=C()

c1.feature1()



						#multiple level inheritence
class A:
	def feature1(self):
		print("feature 1 of A")
	def feature2(self):
 		print("feature 2 of A")

class B:
	def feature3(self):
		print("feature 3 of B")
	def feature4(self):
 		print("feature 4 of B")

class C(A,B):
	pass

a1=A()
b1=B()
c1=C()

c1.feature1()
c1.feature3()


