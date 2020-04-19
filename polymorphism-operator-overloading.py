
# overloading an binary operator (+,-,*)
# built-in method for addition operator(+) supports addition of integers, combining two strings, however does not support addition of two class objects, 
#we can define addition of two class objects using operator overloading (changing the type of arguments/operands of the operator)

class Students: 

    def __init__(self, marks): 
        self.mark = marks

    # adding two objects 
    def __add__(stud1, stud2): 
        return stud1.mark + stud2.mark

    # multiplying two objects
    def __mul__(stud1, stud2):
        return stud1.mark * stud2.mark

    # subtractio of tw objects
    def __sub__(stud1, stud2):
        return stud1.mark - stud2.mark
    
stud1 = Students(12) 
stud2 = Students(6) 

print(stud1 + stud2) 
print(stud1 * stud2)
print(stud1 - stud2)


#Same above program with different arguments 

class Students: 
    def __init__(self, marks): 
        self.mark = marks

    # adding two objects 
    def __add__(a, b):             #a.mark=stud1.mark & b.mark=stud2.mark
        return a.mark + b.mark
    # multiplying two objects
    def __mul__(a, b):
        return a.mark * b.mark

stud1 = Students(12) 
stud2 = Students(6) 

print(stud1 + stud2) 
print(stud1 * stud2)

















