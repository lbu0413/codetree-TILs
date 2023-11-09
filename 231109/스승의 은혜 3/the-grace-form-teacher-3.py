import sys

max_ = -sys.maxsize
N, B = map(int, input().split())
presents = ([tuple(map(int, input().split())) for _ in range(N)])

for i in range(N):
    cnt = 0
    sorted_p = sorted(presents)
    budget = (sorted_p[0][0] // 2) + (sorted_p[0][1])
    for j in range(i + 1, N):
        if budget + sorted_p[j][0] + sorted_p[j][1] <= B:
            budget + sorted_p[j][0] + sorted_p[j][1]
            cnt += 1
    max_ = max(max_, cnt)

print(max_)