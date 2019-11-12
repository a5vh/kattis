pairs = int(input())

while pairs != -1:
    speeds = []
    times = []
    sum = 0

    for i in range(pairs):
        mph, time = input().split()
        speeds.append(int(mph))
        times.append(int(time))


    for i in range(pairs):
        if i == 0:
            sum += speeds[i] * times[i]
        if i > 0:
            sum += speeds[i] * (times[i] - times[i-1]) 
    print(str(sum), " miles")
    pairs = int(input())
