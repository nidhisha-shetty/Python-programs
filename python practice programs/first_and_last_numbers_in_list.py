#Given a list of numbers, return True if first and last number of a list is same

def first_and_last(li):
	if li[0]==li[-1]:
		print("True, first and last numbers are the same")
	else:
		print("False, first and last numbers are not same")

li=li(input("Enter a list of numbers").split(' '))
print(li)
first_and_last(li)
