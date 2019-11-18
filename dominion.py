g, s, c = input().split()
g = int(g)
s = int(s)
c = int(c)

money = 0
vic = " "
treas = " "

for i in range(g):
    money += 3
for i in range(s):
    money += 2
for i in range(c):
    money += 1

if 3 > money >= 0:
    treas = "Copper"
if 6 > money >= 3:
    treas = "Silver"
if money >= 6:
    treas = "Gold"

if 2 > money >= 0:
    vic = "None"
if 5 > money >= 2:
    vic = "Estate"
if 8 > money >= 5:
    vic = "Duchy"
if money >= 8:
    vic = "Province"

if vic == "None":
    print(treas)
else:
    print(vic, "or", treas)
