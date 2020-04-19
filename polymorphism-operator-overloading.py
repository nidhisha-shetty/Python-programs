# a=12
# b=6

# print(a+b)
# print(int.__add__(a,b)) #print(a+b), all the operators(+,*,/,-) behind the scene works as methods (__add__(),----) int is a class with __add__ method
# print(a*b)
# print(int.__mul__(a,b))
# print(a/b)
# print(int.__div__(a,b))
# print(a-b)
# print(int.__sub__(a,b))

# #print(a+b) calls print(int.__add__(a,b))
# #print(a*b) calls print(int.__mul__(a,b))
# #print(a/b) calls print(int.__div__(a,b))
# #print(a-b) calls print(int.__sub__(a,b))




# overloading an binary +,-,* operator 
# built-in method for addition operator(+) supports addition of integers, combining two strings, however does not support addition of two objects, 
#we can define addition of two objects using operator oerloading

class Students: 

    def __init__(self, marks): 
        self.mark = marks

    # adding two objects 
    def __add__(a, b): 
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



##################

#Same above program with different argument names

class Students: 
    def __init__(self, marks): 
        self.mark = marks

    # adding two objects 
    def __add__(a, b): 
        return a.mark + b.mark
        
    def __mul__(a, b):
        return a.mark * b.mark

    
        
stud1 = Students(12) 
stud2 = Students(6) 

print(stud1 + stud2) 
print(stud1 * stud2)

















