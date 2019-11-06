contestants, problems = input().split()
i = 0
contestants = int(contestants)
problems = int(problems)
dict = {}

while i < contestants:
    dict.update({i : input()})
    i += 1

print(problems)