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
