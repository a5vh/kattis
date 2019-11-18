lines = []
for i in range(5):
    lines.append(input())

count = 0
for i in range(len(lines)):
    if "FBI" not in lines[i]:
        count += 1

if count == 5:
    print("HE GOT AWAY!")
else:
    for i in range(len(lines)):
        if "FBI" in lines[i]:
            if i == 4:
                print(i+1)
            else:
                print(i+1, end=" ")
        else:
            if i == 4:
                print()
    