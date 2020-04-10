class Coaching:
    def __init__(self, name, rollno):
        self.n=name
        self.r=rollno
    def student(self):
        print("I am a student", "My name is: "+self.n, "My roll no is: "+self.r)
    
c1=Coaching("neha", "42")
c2=Coaching("priya", "65")
Coaching.student(c1)
c2.student()