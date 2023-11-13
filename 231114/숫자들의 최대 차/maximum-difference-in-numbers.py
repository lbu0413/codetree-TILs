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
        if abs(nums[j] - max(cnt)) > K:
            continue
        else:
            cnt.append(nums[j])

print(len(cnt))