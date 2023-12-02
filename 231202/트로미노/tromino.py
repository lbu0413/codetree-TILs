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



for i in range(n-1):
    for j in range(m-1):
        square = 0
        min_ = 1001
        for k in range(i, i+2):
            for l in range(j, j+2):
                min_ = min(min_, grid[k][l])
                square += grid[k][l]
        square -= min_
        max_ = max(max_, square)

print(max_)