def mysum(*numbers):
    output = 0
    print(type(numbers))
    for num in numbers:
        output += num
    return output

print(mysum(10,20,30,40,100))
