class Employee:
    hike=0.50				               

    def __init__(self, current_salary):
        self.cur_sal=current_salary 	   

    def revised_sal(self):										#instance method because it works with object
        increament=self.cur_sal*Employee.hike
        revised_sal=increament+self.cur_sal
        return(revised_sal)

    def get_cur_sal(self):										#Accessor method(gets/accesses the value) also known as getters, for acessing value of different variable we use different get/accessor methods. 
    	return self.cur_sal

    def set_cur_sal(self, new_salary):							#Mutator method(modifies the value) also known as setters. Constructor (__init__()) is used to set the value, whereas set/mutator method is used to set and modify the value. For modifying value of different variables we use different set/mutator method, hence also known as setters.
    	return self.cur_sal

e1=Employee(500)
e2=Employee(1000)

print(e1.get_cur_sal())											#calling accessor method
print(e2.get_cur_sal())											#calling accessor method

print(e1.set_cur_sal(2000))										#calling mutator method
print(e2.set_cur_sal(3000))										#calling mutator method

print(e1.revised_sal())											#calling instance method
print(e2.revised_sal())											#calling instance method


