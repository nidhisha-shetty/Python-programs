a=34
inp=0
counter=0
while inp!=34:
    inp=int(input("Enter a number"))
    if(inp<a):
        print("Your guess is less than the answer")
        counter+=1
    elif(inp>a):
        print("Your guess is greater than the answer")
        counter+=1
    else:
        print("Your guess is correct")
print("Your total attempts to guess the number was "+ str(counter))
