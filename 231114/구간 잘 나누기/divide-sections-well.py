import sys

max_ = -sys.maxsize
min_ = sys.maxsize

n, m = map(int, input().split())
nums = list(map(int, input().split()))

divider = n // m
for i in range(0, n, divider):
    cnt = 0
    for j in range(i, i + divider):
        cnt += nums[j]
    max_ = max(max_, cnt)
    min_ = min(min_, max_)

print(min_)