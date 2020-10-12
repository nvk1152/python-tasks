# Factorial of a number

# Factorial function
# input: int
# output: int

def factorial(num : int) -> int :
    if num == 0:
        return 1
    else:
        return(num * factorial(num - 1))   # Calls the factorial function again

number = int(input("Enter a number: "))
print(factorial(number))

# 5 * factorial(4)