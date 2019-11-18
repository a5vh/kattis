import math
miles = float(input())

if miles == 0.0:
    print(0)
else:
    print(math.ceil((5280/4854)*(miles*1000)))