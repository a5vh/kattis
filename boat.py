from collections import OrderedDict
parts, days = [int(x) for x in input().split()]
listParts = []

for x in range(days):
    word = input()
    listWord = list(word)

    contains = True
    for c in listWord:
        if 97 <= ord(c) <= 122 or ord(c) == 95:
            contains = True
        else:
            contains = False
    if contains:
        listParts.append(word)

rem = list(OrderedDict.fromkeys(listParts))
if len(rem) >= parts:
    print(listParts.index(rem[-1])+1)
else:
    print("paradox avoided")

    

