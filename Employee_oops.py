class Employee:
    hike=0.50									 	# class variable/static variable

    def __init__(self, current_salary):
        self.cur_sal=current_salary 				# instance variable

    def revised_sal(self):
        increament=self.cur_sal*Employee.hike
        revised_sal=increament+self.cur_sal
        print(revised_sal)

e1=Employee(500)
e2=Employee(1000)

e1.revised_sal()
e2.revised_sal()
