from special_var import *
def CN():
	print("Chennai")
def WB():
	print("West Bengal")

MH()
DL()
CN()
WB()

#"from special_var import *" bydefault executes all the function in "special_var" module, hence the result of this module would be:

# Maharashtra
# Delhi
# Maharashtra
# Delhi
# Chennai
# West Bengal



#Inorder to avoid this, we use "__name__" variable, which holds the value "__main__" for the module which is in execution. For the module which
#is imported as a library, the __name__ variable will have **module name** as the value.

#Add the following code in "special_var.py" program:
# if __name__=="__main__":
# 	main()



