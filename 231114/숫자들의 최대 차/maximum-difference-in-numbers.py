import sys

max_ = -sys.maxsize

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

for i in range(N):
    num = nums[i]
    cnt = [num]
    for j in range(N):
        if i == j:
            continue
        if abs(nums[j] - num) > K:
            continue
        cnt.append(nums[j])
    # max_ = max(max_, cnt)

print(len(cnt))