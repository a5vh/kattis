times = int(input())

for i in range(times):
    b, p = input().split()
    b = float(b)
    p = float(p)
    
    bpm = (60*b)/p
    minAbpm = bpm - (bpm/b)
    maxAbpm = bpm + (bpm/b)

    print("{0:.4f} {1:.4f} {2:.4f}".format(minAbpm, bpm, maxAbpm))
    
    


