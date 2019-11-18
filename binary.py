num = int(input())

num = str(bin(num))
num = num[2::][::-1]
print(int(num, 2))