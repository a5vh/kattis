matrix = [[0 for i in range(4)] for j in range(5)]

for y in range(5):
    matrix[y] = input().split()

for y in range(5):
    for x in range(4):
        matrix[y][x] = int(matrix[y][x])

sums = []
sum = 0

for y in range(5):
    for x in range(4):
        sum += matrix[y][x]
    sums.append(sum) 
    sum = 0

num = max(sums)
print(sums.index(num)+1, num)


    