str='abcdefghabcdefgh'
li=[]
str1=''
li.append(str[0])
for x in str:
    if x in li:
        continue
    else:
        li.append(x)

for x in li:
    str1+=x
print(str1)
