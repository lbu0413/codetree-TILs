import sys

max_ = -sys.maxsize

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]


def get_coins(row, col):
    cnt = 0

    for row in range(N):
        for col in range(N):
            if grid[row][col] == 1:
                cnt += 1
    return cnt

for row in range(N):
    for col in range(N):
        for k in range(1, 3):
            new_row = row + k
            new_col = col + k
            if 0 <= new_row < N and 0 <= new_col < N:
                coins = get_coins(new_row, new_col)
                max_ = max(max_, coins)

            else:
                continue
print(max_)