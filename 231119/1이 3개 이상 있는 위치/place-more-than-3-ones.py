N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir_num = 0

total = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                cnt += board[nx][ny]
        
        if cnt >= 3:
            total += 1

print(total)