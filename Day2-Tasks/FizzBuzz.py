# Fizz Buzz Program

number = input("Enter the limit:")
i = 1
for i in range(1, int(number)+1):
    if i%15 == 0:
        print("Fizz Buzz",end=', ')
    elif i%3 == 0:
        print("Fizz",end=', ')
    elif i%5 == 0:
        print("Buzz",end=', ')
    else:
        print(i,end=', ')
