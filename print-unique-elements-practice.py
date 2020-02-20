str='nidhisha'
str1=''
li=list(str[0])

for x in str:
    if x not in li:
        li.append(x)
for z in li:
    str1+=z
print(str1)
