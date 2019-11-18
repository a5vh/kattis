days = int(input())
temps = [int(x) for x in input().split()]
print(temps)
firstValue = 0

for i in range(len(temps)):
    if i + 2 <= len(temps):
        if temps[i] < temps[i+1] and temps[i+2] < temps[i+1]:
            firstValue = temps[i]
            break
        
print(firstValue)

