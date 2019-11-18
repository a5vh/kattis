from collections import Counter
times = int(input())


for i in range(times):
    nums = int(input())
    numbers = [int(x) for x in input().split()]
    counter = Counter(numbers)
    print("Case #" + str(i+1) + ": " + str(min(counter, key=counter.get)))

