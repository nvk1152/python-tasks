# List comprehension with odd number's squares

numbers = [1, 3, 3, 4, 5, 6]
squares = [x ** 2 for x in numbers if x%2 != 0]
print(squares)