def greet_user():
    """Display a simple greeting""" ## This is a Docstring, which describes what the function does. D
    print("Hello!")

# greet_user()


## Passing info to the function

def greet_user2(username):
    print(f"Hello, {username.title()}!")

# greet_user2('minami')

def display_message():
    print("I am learning python basics")

# display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title}")

# favorite_book("Zero to one")

## Positional Argument demostration
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'ame')

