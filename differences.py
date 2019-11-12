#first get each line of input and put them each into their own aray
#then get each letter from each array and if it is different then put
#a star there otherwise keep the already existing period
    
times = int(input())

for i in range(times):
    firstString = list(input())
    secondString = list(input())
    diff = []

    for i in range(len(firstString)):
        diff.append(".")

    for i in range(len(firstString)):
        if firstString[i] != secondString[i]:
            diff[i] = "*"

    for i in range(len(firstString)):
        print(firstString[i],end="")
    print()
    
    for i in range(len(secondString)):
        print(secondString[i],end="")
    print()

    for i in range(len(diff)):
        print(diff[i],end="")
    print()

    print()



