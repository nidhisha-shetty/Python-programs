class Test():

	def get_data(self): #get_data variable is referring(poiniting) to get_data() object function 
		print("Get data from DB")

def get_monkey_patch_data(): #get_monkey_patch_data variable is referring(poiniting) to get_monkey_patch_data() object function 
	print("Get data from Monkey patch DB")

t1=Test()
t1.get_data=get_monkey_patch_data #now, because of this variable assignment, get_data variable is referring to get_monkey_patch_data() object function; hence "print("Get data from Monkey patch DB")" will be executed on calling get_data()
 
t1.get_data()





