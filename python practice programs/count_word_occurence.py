#Return the total count of sub-string “Emma” appears in the given string

def count_word_occurence(s1):
    temp=[]
    temp+=s1.split(" ")
    occurence=temp.count("Emma")
    print("Emma occured "+ str(occurence) +" times")


s1="Emma is good developer. Emma is a writer"
count_word_occurence(s1)