line = str(input())
chars = []
chars[:0] = line

white = 0
upper = 0
lower = 0
symbols = 0



for i in line:
    if ord(i) == 95:
        white += 1
    if ord(i) >= 65 and ord(i) <= 90:
        upper += 1
    if ord(i) >= 97 and ord(i) <= 122:
        lower += 1
    elif (33 <= ord(i) <= 64) or (123 <= ord(i) <= 126) or (91 <= ord(i) <= 94) or ord(i) == 96:
        symbols += 1

length = len(line)

print(round(float(white/length), 15))
print(round(float(lower/length), 15))
print(round(float(upper/length), 15))
print(round(float(symbols/length), 15))