events = int(input())
days = []

for i in range(events):
    first, last = [int(x) for x in input().split()]
    diff = (last - first)+1
    for i in range(diff):
        days.append(first+i)

print(len(set(days)))