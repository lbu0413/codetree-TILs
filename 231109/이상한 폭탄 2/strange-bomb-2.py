import sys
max_ = -sys.maxsize

N, K = map(int, input().split())

bombs = [int(input()) for _ in range(N)]


explode = False

for i in range(N):
    bombs_in_distance = bombs[i+1:i+K+1]
    if bombs[i] in bombs_in_distance:
        explode = True
        max_ = max(max_, bombs[i])

if explode:
    print(max_)
else:
    print(-1)