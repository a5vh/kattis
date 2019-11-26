sets = int(input())

for i in range(sets):
    setNum, days = [int(x) for x in input().split()]
    candles = 0
    for i in range(days):
        candles += i+1
    candles += days
    print(setNum, candles)
