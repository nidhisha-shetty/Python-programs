#break: It brings the control out of the loop.

#example 1:
x='python'
for i in x:
    if i=='t':
        break
    print("the letter is "+i)
print("loop terminated")

#exanple 2:
for x in range(1,20):
    if x%3==0:
        continue
    print(x)
print("Number is divisible by 3")

#example 3:
avail=5000
x=int(input("Enter the amount"))
while(x<=avail):
    print("Your transaction is being processed, please wait")
    break
else:
    print("Insufficient balance")
print("BYE!!!")


#continue: It brings the control back to the top of the loop.

#example 1:
x='python'
for i in x:
    if i=='t':
        continue
    print("the letter is "+i)
print("Done")

#exanple 2:
for x in range(1,20):
    if x%3==0:
        continue
    print(x)
print("Execution completed")


#pass: The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

#example 1: 
for x in range(1,21):
    if x%2==0:
        pass
        
    else:
        print(x)


#example 2:
for letter in 'Python': 
   if letter == 'h':
      pass
      print('This is pass block')
   print('Current Letter :', letter)

print("Completed")
