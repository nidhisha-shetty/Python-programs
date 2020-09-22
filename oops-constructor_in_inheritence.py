#executes constructor in B only

class A: 

	def __init__(self):
		print("constructor in A")

class B(A): 

	def __init__(self):
		print("constructor in B")

b1=B()

#executes constructor in A, as there is no constructor present in B(extends A)
class A: 

	def __init__(self):
		print("constructor in A")

class B(A): 

	pass

b1=B()


#executes constructor of both classes
class A: 

    def __init__(self):
        print("constructor in A")

class B(A): 

    def __init__(self):
        super().__init__()  			#executes constructor of super class; "super" represents super class
        print("constructor in B")

b1=B()


#Method Resolution Order(MRO) 
class A: 

    def __init__(self):
        print("constructor in A")

class B:

	def __init__(self):
        print("constructor in B")

class C(A, B):             

	def __init__(self):
		super().__init__()               #executes constructor of class A only (though A and B both are super class) due to MRO(executes from left to right)
		print("constructor in C")

c1=C()

# Example: super with instance method
class A: 

    def __init__(self):
        print("constructor in A")

    def f1(self):

     	print("f1-A")

class B:

	def __init__(self):
        print("constructor in B")

    def f1(self):
     	print("f1-B")

class C(A, B):             

	def __init__(self):
		super().f1()              #super with instance method
		print("constructor in C")

c1=C()






