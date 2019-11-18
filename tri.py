x, y, z = [int(x) for x in str(input()).split()]

if x / y == z and x % y == 0:
    print(str(x) + "/" + str(y) + "=" + str(z))
elif y / z == x and y % z == 0:
    print(str(x) + "=" + str(y) + "/" + str(z))

elif x * y == z:
    print(str(x) + "*" + str(y) + "=" + str(z))
elif y * z == x:
    print(str(x) + "=" + str(y) + "*" + str(z))

elif x + y == z:
    print(str(x) + "+" + str(y) + "=" + str(z))
elif y +z == x:
    print(str(x) + "=" + str(y) + "+" + str(z))

elif x - y == z:
    print(str(x) + "-" + str(y) + "=" + str(z))
elif y - z == x:
    print(str(x) + "=" + str(y) + "-" + str(z))
