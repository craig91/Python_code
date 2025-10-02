import sys

myList = []
for i in range(25):
    l = len(myList)
    s = sys.getsizeof(myList)
    print({f'len = {l}, size = {s}'})
    myList.append(i)
