import sys

max_ = -sys.maxsize

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]


def get_coins(row, col, new_row, new_col):
    cnt = 0

    for i in range(row, new_row):
        for j in range(col, new_col):
            if grid[i][j] == 1:
                cnt += 1
    return cnt

for row in range(N):
    for col in range(N):
        for k in range(1, 4):
            new_row = row + k
            new_col = col + k
            if 0 <= new_row < N and 0 <= new_col < N:
                coins = get_coins(row, col, new_row, new_col)
                max_ = max(max_, coins)

            else:
                continue
print(max_)