num = int(input())
number = [int(x) for x in list(str(num))]

#take the number and get its sum then divide the sum by the number until it is mod 0, add 1 if not until it is
sum = 0
for i in range(len(number)):
    sum += number[i]
while num % sum != 0:
    num += 1
print(num)
