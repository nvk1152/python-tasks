# While with else invoking

numbers = [1,2,3,4,5,6,7,8,9]
i = 0
while i < len(numbers):
    num = numbers[i]
    if num % 11 == 0:
        break
    else:
        print(num ** 2, end=', ')
    i += 1
else:
    print("You reached the end of loop")
