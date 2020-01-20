# Program to check if a given sentence is pangram or not 

def check_pangram(str):
    if len(set('abcdefghijklmnopqrstuvwxyz') - set(str)) == 0 :
        return True
    return False
a = input("Enter a string to check for pangram :")
str=set(a)
if check_pangram(str):
	print("It is a pangram")
else:
	print("It is not a pangram")

























