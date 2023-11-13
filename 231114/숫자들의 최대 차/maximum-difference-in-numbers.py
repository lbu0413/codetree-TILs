import sys

max_ = -sys.maxsize

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
cnt = 0


for i in range(N):
    num = nums[i]
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if abs(nums[j] - num) <= 3:
            cnt += 1
    max_ = max(max_, cnt)

print(max_)