atBats = int(input())
sum = 0.0

nums = list(map(int, input().split()))

ok = list(filter((-1).__ne__, nums))

for i in range(len(ok)):
    sum += ok[i]
    
    
print(sum/len(ok))