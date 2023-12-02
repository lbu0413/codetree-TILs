n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_ = 0

for i in range(n):
    for j in range(m):
        horizontal = 0
        for k in range(3):
            if 0 <= j+k < m: 
                horizontal += grid[i][j+k]
        max_ = max(max_, horizontal)

for i in range(n):
    for j in range(m):
        vertical = 0
        for k in range(3):
            if 0 <= i+k < n:
                vertical += grid[i+k][j]
        max_ = max(max_, vertical)


min_ = 1001
for i in range(n):
    for j in range(m):
        square = 0
        for k in range(2):
            for l in range(2):
                if 0 <= i+k < n and 0 <= j+l < m:
                    square += grid[i+k][j+l]
                    min_ = min(min_, grid[i+k][j+l])
        square -= min_
        max_ = max(max_, square)

print(max_)