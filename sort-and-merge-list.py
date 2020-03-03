def sorted_list(li1, li2):
    x=li1.sort()
    y=li2.sort()
    res=[]
    res+=li1+li2
    res.sort()
    print(res)
    
    
    
    
li1=list(input("Enter a list 1"))
li2=list(input("Enter a list 2"))
sorted_list(li1, li2)