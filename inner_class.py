class Human:
	def __init__(self):
		self.innerclass_nose=self.innerclass_nose()
		self.innerclass_eyes=self.innerclass_eyes()
		self.innerclass_brain=self.innerclass_brain()
		print("This is the human body")


		
	class innerclass_nose:
		def __init__(self):
			print("The nose is the body's primary organ of smell and also functions as part of the body's respiratory system.")
	class innerclass_eyes:
		def __init__(self):
			print("Eyes are organs of the visual system.")
	class innerclass_brain:
		def __init__(self):
			print("Brain")
		def func(self):
			print("The human brain is the command center for the human nervous system.")

h1=Human()
h1.innerclass_brain.func()