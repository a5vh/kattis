'''
Ten Hearts - 10
9 Clubs - 0
King Spades(Dominant) - 4
Queen Spades(Dom) = 3
Jack Spades(Dom) = 20
Ten Diamonds = 10
Ace Diamonds = 11
Jack Hearts = 2
'''
times, suit = input().split()
times = int(times)
suit = str(suit)
dominant = {"A":11, "K":4, "Q":3, "J":20, "T":10, "9":14, "8":0, "7":0}
nonDom = {"A":11, "K":4, "Q":3, "J":2, "T":10, "9":0, "8":0, "7":0}
sum = 0

for i in range(times*4):
    card = list(str(input()))
    if card[1] == suit:
        sum += dominant.get(card[0])
    else:
        sum += nonDom.get(card[0])

print(sum)

