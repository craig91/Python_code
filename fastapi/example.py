## Demonstrating type hints

# def getFullName(first_name, last_name):
#     fullName = first_name.title() + " " + last_name.title()
#     return fullName

# now the same function with type hints

def getFullName(first_name: str, last_name: str):
    fullName = first_name.title() + " " + last_name.title()
    return fullName


print(getFullName("Haruto", "Tsunoda"))