print(type('Hello, how are you'))

username = 'Super Coder'
password = 'Super secret'

long_string = '''
WOW
0 0
___

'''

print(long_string)

print('My ' + 'name ' + 'is ' + 'craig ')

first_name = "Craig "
last_name = "Dejean "
full_name = first_name + last_name

print(full_name)

# Type conversion

# print(type(str(100))) # Converts an int into a str type

# print(type(int(str(100)))) # The conversion starts from the right most function:  type() <-- int() <-- str() so the output will be an int
# the function directly above is the same as the one below
a = str(100)
b = int(a)
c = type(b)

print(c)


# Escape Sequences
# weather = " \t It\'s \"kind of\" Sunny \n hope you have a good day!"
# print(weather)

# Formatted Strings
name = 'Johnny'
age = 55

# Without format
print('hi ' + name + '. You are ' + str(age) + ' years old')

# With format
print(f'hi {name}. You are {age} years old')

# This f is a new feature of python 3

# python2 style
print('hi {}. You are {} years old'.format(name, age))