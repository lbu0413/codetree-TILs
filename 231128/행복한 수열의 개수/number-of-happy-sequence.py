N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    row = grid[i]
    permutation_cnt = 1
    for j in range(N - 1):
        if row[j] == row[j + 1]:
            permutation_cnt += 1
        
        if permutation_cnt >= M:
            cnt += 1
            break



for i in range(N):
    permutation_cnt = 1
    for j in range(N-1):
        if grid[j][i] == grid[j + 1][i]:
            permutation_cnt += 1
        
        if permutation_cnt >= M:
            cnt += 1
            break

if M == 1:
    print(N * 2)
else:
    print(cnt)