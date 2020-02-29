def combine_ele(li1, li2):
    range_value=[]
    for x in range(len(li1)):
        range_value+=li1[x]
        range_value+=str(li2[x])
    print(range_value)
li1=['a','b','c']
li2=[4,5,6]
combine_ele(li1, li2)
