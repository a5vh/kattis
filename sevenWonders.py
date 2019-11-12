cards = list(input())
t = 0
c = 0
g = 0
sum = 0

for card in cards:
    if card == "T":
        t += 1
    if card == "C":
        c += 1
    if card == "G":
        g += 1

sum += pow(t, 2)
sum += pow(c, 2)
sum += pow(g, 2)
if t > 0 and c > 0 and g > 0:
    sum += 7
print(sum)
