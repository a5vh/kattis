moves = list(input())
cups = [1, 2, 3]
temp = 0

for move in moves:
    if move == "A":
        temp = cups[0]
        cups[0] = cups[1]
        cups[1] = temp
    if move == "B":
        temp = cups[1]
        cups[1] = cups[2]
        cups[2] = temp
    if move == "C":
        temp = cups[0]
        cups[0] = cups[2]
        cups[2] = temp

if cups[0] == 1:
    print(1)
if cups[1] == 1:
    print(2)
if cups[2] == 1:
    print(3)
    


