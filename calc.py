#Modules
#Project A(calc.py) has features such as addition and subtraction, Project B(calc_1.py) has features such as addition, subtraction, multiplication, and division.
#Therefore, will import addition and subtraction features from Project A to Project B and not create them in Project B.

#These are basically used in large projects so instead of having one large module we can have multiple modules and import them.
#NOTE: Both the files should be in the same directory


a=5
b=3

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

res1=add(a,b)
res2=sub(a,b)

print(res1)
print(res2)
