a, b = [int(x) for x in input().split()]

while a and b != 0:
    remainder = a % b
    whole = int(a / b)
    print(whole, remainder, "/", b)
    a, b = [int(x) for x in input().split()]
    
