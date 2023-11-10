import sys

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
max_ = 0

for i in range(N):
    for j in range(N-3+1):
        cnt = 0
        for k in range(j, j+3):
            cnt += board[i][j+k]
        max_ = max(max_, cnt)

print(max_)