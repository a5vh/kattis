cases = int(input())

for i in range(cases):
    a, b, c = [int(x) for x in input().split()]

    if a * b == c:
        print("Possible")
    elif b / a == c or a / b == c:
        print("Possible")
    elif a + b == c:
        print("Possible")
    elif a - b == c or b - a == c:
        print("Possible")
    else:
        print("Impossible")

