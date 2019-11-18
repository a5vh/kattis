import math as m
d, v = input().split()
d = int(d)
v = int(v)

while d != 0 and v != 0:
    #get diameter to get area
    # v of cylinder is pir^2height
    d3 = d*d*d - 6*v/(m.pi)
    print(round(m.pow(d3, 1/3.0), 9))
    d, v = input().split()
    d = int(d)
    v = int(v)