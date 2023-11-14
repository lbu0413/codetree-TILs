import sys

max_ = -sys.maxsize
ans = sys.maxsize

n, m = map(int, input().split())
nums = list(map(int, input().split()))

divider = n // m
minFinder = []
for i in range(0, n, divider):
    cnt = 0
    for j in range(i, i + divider):
        cnt += nums[j]
    max_ = max(max_, cnt)

    if divider == 1:
        ans = max_
    else:
        ans = min(ans, max_)

print(ans)