#Errors can happen in programs, and we need a clean way to handle them
# This code will cause an derror because you can't divide by zero:
# x = 10 / 0

# try:
#     x = 10 / 0
# except:
#     print("Well that didn't work!")


from multiprocessing.sharedctypes import Value
from zlib import Z_DEFAULT_STRATEGY


try:
    answer = input("What should I divide 10 by? ")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:
    print("This code always runs")