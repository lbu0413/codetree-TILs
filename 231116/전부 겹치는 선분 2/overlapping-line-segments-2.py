import sys

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

def check_overlap(line1, line2):
    return not(line1[1] < line2[0] or line2[1] < line1[0])

ans = "No"

for i in range(N):
    for j in range(N - 1):
        if i == j:
            continue
        if check_overlap(lines[j], lines[j + 1]):
            print("Yes")
            sys.exit()

print("No")