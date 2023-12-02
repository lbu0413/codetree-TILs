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
        one, two, three, four = 0, 0, 0, 0
        for k in range(2):
            if 0 <= i+k < n and 0 <= j+k < m:
                one += grid[i+1][j+k]
                two += grid[i+1][j+k]
                three += grid[i][j+k]
                four += grid[i][j+k]
        
        one += grid[i][j]
        two += grid[i][j+1]
        three += grid[i][j+1]
        four += grid[i+1][j]
        max_ = max(max_, one, two, three, four)

print(max_)