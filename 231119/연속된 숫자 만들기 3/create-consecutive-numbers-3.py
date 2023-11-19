a, b, c = map(int, input().split())


if b - a == 1 and c - b == 1:
    print(0)

elif b - a == 2 and c - b == 2:
    print(1)

elif b - a == 3 or c - b == 3:
    print(2)

else:
    print(3)