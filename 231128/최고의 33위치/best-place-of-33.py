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
        new_row = row + 2
        new_col = col + 2

        if new_row >= N or new_col >= N:
            continue
        
        coins = get_coins(new_row, new_col)

        max_ = max(max_, coins)

print(max_)