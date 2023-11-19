a, b, c = map(int, input().split())


if b - a == 1 and c - b == 1:
    print(0)

elif b - a == 2 and c - b == 2:
    print(1)

else:
    cnt = 0
    if b - a < c - b:
        while b - a != 1 or c - b != 1:
            a = b
            b = b + 1
            cnt += 1
        
    else:
        while b - a != 1 or c - b != 1:
            c = b
            b = b - 1
            cnt += 1
    print(cnt)