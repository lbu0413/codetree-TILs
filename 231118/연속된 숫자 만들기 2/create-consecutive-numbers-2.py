a, b, c = map(int, input().split())

if b - a == 1 and c - b == 1 and c - a == 2:
    print(0)

if c - b == 2:
    print(1)

else:
    print(2)