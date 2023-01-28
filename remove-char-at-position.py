# Remove character at ith position from string

def removechar():
    string = "Pythonprogramming"
    i=12
    res=''
    for x in range(len(string)):
        if x!=i:
            res=res+string[x]
    return res
print(removechar())
