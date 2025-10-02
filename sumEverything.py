def sumEverything(*args):
    if not args:
        return args
    output = args[0]
    for item in args[1:]:
        print(args[1:])
        output += item
    return output
print(sumEverything('abc', 'def'))
