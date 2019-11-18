import math as m
h, v = input().split()
h = int(h)
v = int(v)

print(m.ceil(h/m.sin(m.radians(v))))

