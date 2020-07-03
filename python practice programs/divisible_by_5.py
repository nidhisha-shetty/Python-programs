# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def divisible_by_5(li):
    for x in li:
        if int(x)%5==0:
            print("Number divisible by 5 is "+x)
    

li=list(input("Enter a list of numbers").split(','))
divisible_by_5(li)