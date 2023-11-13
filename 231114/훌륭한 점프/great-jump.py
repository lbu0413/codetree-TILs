import sys

MAX = 100 + 1

n, k = map(int, input().split())
nums = list(map(int, input().split()))


def isPossible(limit):
    last_idx = 0
    for i in range(1, n):
        if nums[i] <= limit:
            if i - last_idx > k:
                return False
            last_idx = i
    
    return True




min_ = 0
for a in range(max(nums[0], nums[-1]), MAX):
    if isPossible(a):
        print(a)
        break