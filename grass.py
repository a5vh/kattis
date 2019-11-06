cost = float(input())
L = int(input())
sum = 0.0

for i in range(L):
    width, length = input().split()
    width = float(width)
    length = float(length)
    sum += (width*length)*cost
print(float(sum))