import sys

N = int(input())

lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

for i in range(N):
    x, y = lines[i]

    for j in range(N):
        if i == j:
            continue
        a, b = lines[j]
        if a > y:
            print("No")
            sys.exit()
    else:
        print("Yes")
        sys.exit()