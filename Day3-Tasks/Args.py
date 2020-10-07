# Using variable args to implement sum function that sums all the args passed to it

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum(1, 2, 3))
print(sum())
print(sum(5, 7))