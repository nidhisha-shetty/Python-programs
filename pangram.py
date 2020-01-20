#Assignment for 9/6/2019

# def pangram(string):
# 	alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 	for x in range(len(string)):
# 		if x in alphabets:
# 			print("pangram")
# 		else:
# 			print("not pangram")


# pangram("The quick brown fox jumps over the lazy dog")



# def pangram(string):
# 	alphabets='abcdefghijklmnopqrstuvwxyz'
	
# 	for x in alphabets:
# 		if x in string:
# 			print("True")
		
# 	return(False)

# pangram("The quick brown fox jumps over the lazy do")

# def panagram(string):
#     check="abcdefghijklmnopqrstuvwxyz"
#     for l in check:
#         if(l in string):
#             continue
#         else:
#             return False
#     return True    
# a=panagram("The quick brown fox jumps over the lazy do")       
# #n=input("Enter Any Text:")
# if(panagram(:
#     print("Yes It is a Pangram")
# else:

#     print("No It is not a Pangram")



# def pangram(str):
# 	a={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
# 	#if(len(set(str)-set(\len(a))==0):
# 	if len(set(a)-set(str.lower()))==0:
# 		return(True)
# 	else:
# 		return(False)
# b=input("Please enter a string:")
# if(pangram(b)):	
# 	print("pangram")
# else:
# 	print("Not pangram")
#res=pangram("The quick brown fox jumps over the lazy dog")):
#	print("Pangram")
#else:
#	print("Not pangram")


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






# if(check_pangram(user_str)):
#     print("It is a pangram string")
# else:
# 	print("It is not a pangram string")























