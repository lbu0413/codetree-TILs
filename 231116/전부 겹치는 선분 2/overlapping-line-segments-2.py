import sys

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(N - 1):
        if i == j:
            continue
        if not (lines[j][1] < lines[j + 1][0]) or not(lines[j + 1][1] < lines[j][0]):
            print("Yes")
            sys.exit()

print("No")