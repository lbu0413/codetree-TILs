import sys

min_ = sys.maxsize

N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

def diff_(i, j):
    x1, y1 = dots[i]
    x2, y2 = dots[j]
    return (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        min_ = min(min_, diff_(i,j))

print(min_)