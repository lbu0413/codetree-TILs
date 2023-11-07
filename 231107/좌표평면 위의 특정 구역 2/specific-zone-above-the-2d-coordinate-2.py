import sys

min_ = sys.maxsize

N = int(input())

points = [tuple(map(int, input().split())) for _ in range(N)]


for i in range(N):
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for j, (x, y) in enumerate(points):
        if i == j:
            continue
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    area = (max_x - min_x) * (max_y - min_y)
    min_ = min(min_, area)

print(min_)