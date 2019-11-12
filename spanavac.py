h, m = input().split()
h = int(h)
m = int(m)

if m - 45 < 0:
    m = 60 - abs(m - 45)
    if h - 1 < 0:
        h = 23
    else:
        h -= 1
else:
    m -= 45

print(str(h), str(m))