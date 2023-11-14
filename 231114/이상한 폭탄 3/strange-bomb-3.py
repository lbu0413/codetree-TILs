N, K = map(int, input().split())
MAX = 1000000
arr = [0] * MAX
bombs = [int(input()) for _ in range(N)]


for i in range(N):
    the_bomb = bombs[i]
    for j in range(i - K, K + 1):
        if i == j:
            continue
        if j < 0 or j >= N:
            continue
        if the_bomb == bombs[j]:
            arr[bombs[j]] += 1


max_bomb = max(arr)

if max_bomb == 0:
    print(0)

else:
    print(arr.index(max_bomb))