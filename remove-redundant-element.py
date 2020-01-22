def red(string):
    li=[]
    li.append(string[0])
    for x in string:
        if x!=li[-1]:
            li.append(x)
    print(li)
    
red("aaaaabbaaccdeffgggh")