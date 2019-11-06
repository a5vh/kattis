times = input()
times = int(times)
sum = 0

for i in range(times):
    num = input()
    lastNum = int(num[-1])
    otherNum = int(num[0:-1])
    sum += pow(otherNum, lastNum)
print(sum)