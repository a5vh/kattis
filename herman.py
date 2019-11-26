import math as m
r = int(input())

print('%.6f' % ((m.pi)*(r*r)))

edges = (r*2)*4
inPi = edges/(2*r)
a = inPi*(r*r)

print('%.6f' % (a/2))