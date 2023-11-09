N, K = map(int, input().split())

bombs = [int(input()) for _ in range(N)]

max_ = -1
for i in range(N):
    bombs_in_distance = bombs[i+1:i+K+1]
    if bombs[i] in bombs_in_distance:
        max_ = max(bombs_in_distance)

print(max_)