import sys


N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    min_x = sys.maxsize
    min_y = sys.maxsize
    for j in range(N):
        if i == j:
            continue
        x_diff = abs(dots[i][0] - dots[j][0])
        y_diff = abs(dots[i][1] - dots[j][1])
        
        min_x = min(min_x, x_diff)
        min_y = min(min_y, y_diff)

    ans = (min_x * min_x) + (min_y * min_y)
print(ans)