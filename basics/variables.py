# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myInt = 5
myFloat = 13.2
myStr = "This is a string"
myBool = True
myList = [0, 1, "two", 3.2, False]
myTuple = (0, 1, 2)
myDict = {"One" : 1, "Two" : 2}

print(myInt)
print(myFloat)
print(myStr)
print(myBool)
print(myList)
print(myTuple)
print(myDict)


# re-declaring a variable works
myInt = "abc"
print(myInt)

# to access a member of a sequence type, use []
print(myList[2])
print(myTuple[1])


# use slices to get parts of a sequence
print(myList[1:5])