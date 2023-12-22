def greet_user():
    """Display a simple greeting""" ## This is a Docstring, which describes what the function does. D
    print("Hello!")

greet_user()


## Passing info to the function

def greet_user2(username):
    print(f"Hello, {username.title()}!")

greet_user2('minami')

def display_message():
    print("I am learning python basics")

display_message()