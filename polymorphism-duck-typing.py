# Polymorphism: multiple forms
# If there exists an object, and the object has the said method, (not concerned with which class' object it is) it is known as Duck typing

class Java:
	def execute(self):
		print("Exclipse")
		print("jdk")

class Csharp:
	def execute(self):
		print("Visual Studio")

class Laptop:
	def execute(self, ide):  #"ide" is the object of a class (Jave/Csharp)
		ide.execute()		 #"execute" is the method of the object

ide=Csharp() #ide=Java() 
l1=Laptop()
l1.execute(ide)
