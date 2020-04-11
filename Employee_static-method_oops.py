#Static method knows nothing about the class and just deals with the parameters.

# class Employee:
#     @staticmethod
#     def count_of_employee():                #staticmethod accepts neither object nor class as an argument, it doesnot work with instance variables nor with class variables, it acts as  an independent function.
#         emp_count=0
#         emp_list=['e1','e2','e3','e4','e5']
#         for emp in emp_list:
#             emp_count+=1
#         return emp_count
# print(Employee.count_of_employee())




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
    
    @classmethod
    def get_cur_sal(cls):
    	print("Hike for all the employess with salary less than 1k is "+str(cls.hike_1k) +" percent")
    	print("Hike for all the employess with salary between 1k - 2k is "+str(cls.hike_2k) +" percent")

    @staticmethod
    def count_of_emp():
        emp_Count=0
        for emp in emp_list:
           emp_Count+=1
        return emp_Count

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

print("The total number of employees are "+str(Employee.count_of_emp()))

   

