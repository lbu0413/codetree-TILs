from collections import deque

N = int(input())

original_nums = list(range(1, N + 1))
nums = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if nums[i] != original_nums[i]:
        cnt += 1

print(cnt + 1)