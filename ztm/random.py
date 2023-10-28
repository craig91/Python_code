from datetime import date


current_year = date.today()
current_year = current_year.year


# birth_year = int(input('What year were you born? '))

#age = current_year - birth_year

#your_birth_year = f'Your age is: {age}'
# print(your_birth_year)



# Password Checker

# ask for username 
username = input("What is your username?: ")

# ask for password
password = input("What is your password?: ")
password_length = len(password)
obfuscate = '*' * password_length

print(f'{username}, your password {obfuscate} is {password_length} characters long')
