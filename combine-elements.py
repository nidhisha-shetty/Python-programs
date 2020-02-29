#combining elements of two lists with unequal lengths alternatively
def combine_ele(li1, li2):
    range_value=[]
    range_value+=str(len(li1))
    range_value+=str(len(li2))
    range_value.sort()
    res=[]
    for x in range(int(range_value[-1])):
        if x in range(len(li1)):
            res+=str(li1[x])
        if x in range(len(li2)):
            res+=str(li2[x])
    
    
    # res=[str(a) + str(b) for a, b in zip(li1, li2)]
    #res=list(zip(li1, li2))
    print(res)

li1=['a','b','c','d','e']
li2=[4,5,6]
combine_ele(li1, li2)


