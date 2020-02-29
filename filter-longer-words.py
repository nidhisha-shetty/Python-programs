def filter_long_words(li1, num ):
    for x in li1:
        if len(x) > num:
            print("The word longer than the number is: "+x)
            
li1=['nidhisha', 'shetty', 'python']
num=int(input("Enter a number"))
filter_long_words(li1, num)