a, b = input().split()

a = a[::-1]
b = b[::-1]

if a > b:
    print(a)
elif b > a:
    print(b)