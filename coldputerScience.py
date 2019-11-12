times = int(input())

line = input().split()
negative = 0

for i in range(len(line)):
    if int(line[i]) < 0:
        negative += 1

print(negative)

