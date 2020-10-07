# Guessing Game

lucky_number = 9
response = input("Do you want to guess the number(y/n):")
while response != "n":
    number = input("Guess the number:")
    user_number = int(number)
    if user_number == lucky_number:
        print("Congratulations! You guessed it correctly")
    else:
        print(f"Sorry! You missed the number by difference {abs(user_number-lucky_number)}")
    response = input("Do you want to guess the number(y/n):")
