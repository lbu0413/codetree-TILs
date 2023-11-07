import sys
max_ = -sys.maxsize

N = int(input())
working_time = [tuple(map(int, input().split())) for _ in range(N)]


for i in range(N):
    total_ = 0
    for j in range(N):
        if i == j:
            continue
        start, end = working_time[j]
        total_ += (end - start + 1)

        max_ = max(max_, total_)

print(max_)