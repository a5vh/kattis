line = input().split()

if len(line) != len(set(line)):
    print("no")
else:
    print("yes")