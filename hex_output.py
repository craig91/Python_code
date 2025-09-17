def hex_output():
    decNum = 0
    hexNum = input("Input a hexidecimal number:")
    for index, i in enumerate(reversed(hexNum)):
        decNum += int(i, 16) * (16 ** index)
    print(decNum)

hex_output()
