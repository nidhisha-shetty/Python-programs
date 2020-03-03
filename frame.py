#Function that takes a list of strings and prints them, one per line, in a rectangular frame.

def frame(li1):
    print("**********")
    for x in li1:
        print("*"+x,end=''+"*")
        print()
    print("**********")
     
li1=list(input("Enter a list of strings").split(","))
frame(li1)
