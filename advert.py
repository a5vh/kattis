times = int(input())
for i in range(times):
    r, e, c = input().split()
    r = int(r)
    e = int(e)
    c = int(c)
    
    if r + c == e:
        print("does not matter")
    elif r + c < e:
        print("advertise")
    elif r + c > e:
        print("do not advertise")