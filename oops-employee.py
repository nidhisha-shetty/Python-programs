```
class Employee:
	def emp(self):
		print("Heena, 2124, Mumbai")

e1 = Employee()                           #Creating objects of class
e2 = Employee()
e3 = Employee()

e1.emp()                                  #calling function using the objects, alternatively "Employee.emp(e1)" can also be used to call the function
e2.emp()
e3.emp()
```

#The above program will print the same data for all employees, inorder to have unique data for each employee, we use __init__() method:

```
class Employee:

	def __init__(self, name, id, place):     #called on object creation. name, id, place are the arguments passed to __init__ method. self is the object(e1, e2, e3) currently in execution.
		
		self.name=name                         #assigning values to object
		self.id=id
		self.place=place

	def emp(self):
		print("Employee details are: "+self.name +" "+self.id+" "+self.place )


e1 = Employee("Heena", "2124", "Mumbai") 
e2 = Employee("Nidhisha", "2126", "Delhi")
e3 = Employee("Ria", "2134", "Chennai")

e1.emp()
e2.emp()
e3.emp()
```
