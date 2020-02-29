def find_longest_words(li1):
    final=[]
    for x in li1:
        value=len(x)
        final+=str(value)
    final.sort()
    print("The length of the longest word is: "+final[-1])
        
li1=['nidhisha', 'shetty', 'python']
find_longest_words(li1)
