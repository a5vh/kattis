pieces = input().split()

for i in range(len(pieces)):
    pieces[i] = int(pieces[i])

if pieces[0] != 1:
    print(1 - pieces[0], end=" ")
else:
    print(0, end=" ")

if pieces[1] != 1:
    print(1 - pieces[1], end=" ")
else:
    print(0, end=" ")

if pieces[2] != 2:
    print(2 - pieces[2], end=" ")
else:
    print(0, end=" ")

if pieces[3] != 2:
    print(2 - pieces[3], end=" ")
else:
    print(0, end=" ")

if pieces[4] != 2:
    print(2 - pieces[3], end=" ")
else:
    print(0, end=" ")

if pieces[5] != 8:
    print(8 - pieces[3], end="")
else:
    print(0, end="")
print()