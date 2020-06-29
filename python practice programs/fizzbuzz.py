#From 1-100 if the number is divisible by 3, print 'Fizz', if divisible by 5, print 'Buzz', if divisble by both 3 and 5, print 'FizzBuzz', else print the number

for x in range(1,100):
    if x % 3==0 and x%5!=0:
        print("Fizz")
    elif x%5==0 and x%3!=0:
        print("Buzz")
    elif x%5==0 and x%3==0:
        print("FizzBuzz")
    else:
        print(x)