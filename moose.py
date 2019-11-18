l, r = input().split()
l = int(l)
r = int(r)
points = 0

if l > r:
    points = l*2
else:
    points = r*2

if l != r:
    print("Odd", points)
elif (l != 0):
    print("Even", points)
else:
    print("Not a moose")




