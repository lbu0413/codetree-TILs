from collections import deque

N = int(input())

nums = list(map(int, input().split()))


idx = N - 2

while idx >= 0 and nums[idx] < nums[idx + 1]:
    idx -= 1

print(idx + 1)