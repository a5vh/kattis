numLines = int(input())
i = 0
sum = 0

while i < numLines:
    x, y = input().split()
    x = float(x)
    y = float(y)
    sum += (x*y)
    i += 1

print(sum)