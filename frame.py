def frame(li1):
    print("**********")
    for x in li1:
        
        print("*"+x,end=''+"*")
        print()
    
    print("**********")
    
    
li1=list(input("Enter a list of strings").split(","))
frame(li1)