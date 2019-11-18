presses = int(input())
a = 1
b = 0

for i in range(presses):
    temp = b
    b += a
    a += temp

print(a, b)