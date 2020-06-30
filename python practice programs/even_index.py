#print characters which are displayed on even index numbers
def even_index(var):
    for x in range(len(var)):
        if x%2==0:
            print("index["+str(x)+"] is "+var[x])
var=input("Enter a word ")
even_index(var)

#print(var[0:6:2]) ##alternate single line solution
