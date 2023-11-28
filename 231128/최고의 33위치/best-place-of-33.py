import sys

max_ = -sys.maxsize

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]


def get_coins(row, col, new_row, new_col):
    cnt = 0
    for i in range(row, new_row + 1):
        for j in range(col, new_col + 1):
            if grid[i][j] == 1:
                cnt += 1
    return cnt

for row in range(N):
    for col in range(N):
        new_row = row + 2
        new_col = col + 2
        if 0 <= new_row < N and 0 <= new_col < N:
            coins = get_coins(row, col, new_row, new_col)
    
    max_ = max(max_, coins)
        
print(max_)