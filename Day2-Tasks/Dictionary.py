# Dictionary with sqaures from 1 to 5 and their values multiplied

squares = {"1" : 1, "2" : 4, "3" : 9, "4" : 16, "5" : 25}
multiplied = [value * 2 for key, value in squares.items()]
print(multiplied)