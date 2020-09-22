#Inorder to avoid importing class (if it is used for one other class) we can use inner/nested class
class Human:
	
	def __init__(self):
		self.innerclass_nose=self.innerclass_nose()
		self.innerclass_eyes=self.innerclass_eyes()
		self.innerclass_brain=self.innerclass_brain()
		print("This is the human body")
		
	class innerclass_nose:
		
		def __init__(self):
			print("Nose class.")
			
	class innerclass_eyes:
		
		def __init__(self):
			print("Eyes class.")
			
	class innerclass_brain:
		
		def __init__(self):
			print("Brain class")
			
		def func(self):
			print("The human brain is the command center for the human nervous system.")

h1=Human()
h1.innerclass_brain.func()
