#for a number in the range from 1 to 10, print the sum of current number and the previous number

def sum_current_previous(n):
    y=0
    for x in range(n):
        res=x+y
        print(res)
        y=x
sum_current_previous(11)