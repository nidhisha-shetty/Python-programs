# Calculate income tax for the given income by following the given rules: First 10000 - 0%, Second 10000 - 10%, Amount>20000 - 20%
income=int(input("Enter the number"))
if income<=10000:
    tax=0
    print(tax)
elif income<=20000:
    tax=((income-10000)*10)/100
    print(tax)
else:
    tax=0
    tax=tax+(10000*10)/100
    tax=tax+((income-20000)*20)/100
    print(tax)