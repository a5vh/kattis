from collections import Counter
times = int(input())
for i in range(times):
    num = int(input())
    places = []
    for i in range(num):
        places.append(str(input()))
    
    Counter(places).keys()
    for place in Counter(places).values():
        print(place)
