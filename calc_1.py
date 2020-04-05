#Modules
#Project A(calc.py) has features such as addition and subtraction, Project B(calc_1.py) has features such as addition, subtraction, multiplication, and division.
#Therefore, will import addition and subtraction features from Project A to Project B and not create them in Project B.
#These are basically used in large projects so instead of having one large module we can have multiple modules and import them.
#NOTE: Both the files should be in the same directory


##Project B(calc_1.py) having add, sub, mul, and div functions, importing add and sub functions from "calc.py"

from calc import *          		#or "import calc"

x=7
y=9

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

res1= add(x,y)				#if "import calc" on line 1 then "calc.add(x,y)"  
res2= sub(x,y)				#if "import calc" on line 1 then "calc.sub(x,y)"
res3= mul(x,y)			 	
res4= div(x,y)				

print(res1)
print(res2)
print(res3)			
print(res4)
