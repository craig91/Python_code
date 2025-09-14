def aver(*numbers):
    output = 0
    for digits in numbers:
            output += digits
    return output / 2
    


print("averge for sum", aver(10,20,30,40,50))