from collections import Counter

num = [1,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,4]
cnt = Counter(num)
print(cnt)


thisTuple = ("apple",)
print(type(thisTuple))

fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruit:
    if "a" in x:
        newList.append(x)

print(newList)

