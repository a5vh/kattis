times = int(input())
for i in range(times):
    num = int(input())
    if num % 2 == 0:
        print(num, " is even")
    elif num % 2 != 0:
        print(num, " is odd")