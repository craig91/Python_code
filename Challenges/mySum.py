def mySum(*numbers):
    output = 0
    for num in numbers:
        output += num
    return output


print(mySum(2,3,3,3,5,6,8,3,234,6,6245,253))
