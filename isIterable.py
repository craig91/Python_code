def isIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


print(isIterable("a string"))
print(isIterable([1,2,3]))
print(isIterable(5))



