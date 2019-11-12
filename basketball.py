from textwrap import wrap

line = str(input())
score = wrap(line, 2)

a = 0
b = 0

for pair in score:
    ok = list(pair)
    if ok[0] == "A":
        a += int(ok[1])
    if ok[0] == "B":
        b += int(ok[1])

if a > b:
    print("A")
else:
    print("B")
