rot, string = input().split()
rot = int(rot)

while rot != 0:
    string = string[::-1]
    print(string)
    rot, string = input().split()
    rot = int(rot)
