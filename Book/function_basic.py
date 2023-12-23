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

# describe_pet('cat', 'ame')
# describe_pet(pet_name='jacob', animal_type='alpaca') ## keyword arg ignores order

def describe_pet2(pet_name2, animal_type2='dog'):
    print(f"\nI have a {animal_type2}")
    print(f"His name is {pet_name2.title()}")

# describe_pet2("Jimmy")
# describe_pet2("mr.oink", animal_type2='pig', ) ## when using a default value, positional args apply in this case.

def make_shirt(size, message):
    print(f"\nYour shirt size is: {size}")
    print(f"And the message is: {message}")

def make_shirt2(size="Large", message="I love python"):
    print(f"\nYour shirt size is: {size}")
    print(f"The message on the shirt says: {message}")



make_shirt("Large", "I am too sexy for this shirt")
make_shirt(message="I am a baseball fan", size="Medium")
make_shirt2()

def describe_city(city, country):
    print(f"\n{city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Cape Town", "South Africa")
describe_city("Moscow", "Russia")