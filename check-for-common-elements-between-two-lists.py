#If there exists a common element between two lists, return True, else False
def overlapping(li1, li2):
    for x in li1:
        if x in li2:
            print("True")
            break
    else:
        print("False")

li1=[1,2,3]
li2=[3,4,5]

res=overlapping(li1, li2)
