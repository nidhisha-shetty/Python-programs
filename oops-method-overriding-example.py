'''
P.S: Implement method overriding, if the numbers are greater than 100 then execute calculate() of child class else execute calculate() of parent class.
'''

#Solution:
class Parent():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calculate(self):
        res = self.num1 + self.num2
        return res

class Child(Parent):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def calculate(self):
        if self.num1 < 100 and self.num2 <100:
            return super().calculate()
        else:
            res = self.num1 * self.num2
            return res

num1 = 30
num2 = 60

c1 = Child(num1, num2)
print(c1.calculate())
