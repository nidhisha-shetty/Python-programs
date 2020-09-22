#A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance.

# class Employee:
# 	emp_comp="BrowserStack"				#class variable
# 	emp_dept="Engineering"				#class variable

# 	@classmethod						
# 	def emp_info(cls):				#class method
# 		return cls.emp_comp
# 	@classmethod	
# 	def emp_info_dept(cls):				#class method
# 		return cls.emp_dept

# print(Employee.emp_info())
# print(Employee.emp_info_dept())

class Employee:
    hike_1k=0.50				               
    hike_2k=0.25

    def __init__(self, current_salary):
        self.cur_sal=current_salary 	   

    def revised_sal_1k(self):										
        increament=self.cur_sal*Employee.hike_1k
        revised_sal=increament+self.cur_sal
        return(revised_sal)

    def revised_sal_2k(self):										
        increament=self.cur_sal*Employee.hike_2k
        revised_sal=increament+self.cur_sal
        return(revised_sal)
        
    @classmethod              			 #classmethod is executed irrespective of object creation
    def get_cur_sal(cls):
    	print("Hike for all the employess with salary less than 1k is "+str(cls.hike_1k) +" percent")
    	print("Hike for all the employess with salary between 1k - 2k is "+str(cls.hike_2k) +" percent")

   
e1=Employee(500)
e2=Employee(700)
e3=Employee(800)
e4=Employee(1200)
e5=Employee(1500)

Employee.get_cur_sal()		

emp_list=[e1,e2,e3,e4,e5]
for emp in emp_list:
	if emp.cur_sal <= 1000:
		print(emp.revised_sal_1k())				
	else:
		print(emp.revised_sal_2k()) 							
