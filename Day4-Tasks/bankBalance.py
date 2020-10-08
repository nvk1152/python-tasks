# Securing Function to display balance

import functools

user = {"username" : "vamsi", "password" : "qwerty", "balance" : 25385.56}

def validation(func):
    @functools.wraps(func)
    def authentication(*args, **kwargs):
        if user["username"] == args[0]:
            if user["password"] == args[1]:
                return func(*args, **kwargs)
            else:
                print("Invalid Credentials!")
        else:
            print("Invalid Credentials!")
    return authentication

@validation
def showBalance(username : str, password : str) -> float:
    return user["balance"]

username = input("Enter Username: ")
password = input("Enter Password: ")
balance = showBalance(username, password)
if(balance != "None"):
    print("Your balance is: Rs.", balance)