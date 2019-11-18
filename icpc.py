numUniv = int(input())
univ = []
winners = {}


for i in range(numUniv):
    univ.append(input())

for uni in univ:
    un, team = uni.split()
    if len(winners) < 12:
        if un not in winners:
            winners.update({un:team})
    
for i, j in winners.items():
    print(i, j)



