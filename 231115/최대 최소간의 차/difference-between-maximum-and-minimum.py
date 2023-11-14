import sys
N, K = map(int, input().split())

nums = list(map(int, input().split()))

MAX = 10000 + 1

min_ = sys.maxsize


for i in range(1, MAX):
    cost = 0
    for num in nums:
        if i <= num and num <= i + K:
            continue
        
        elif i > num:
            cost += (i - num)
        
        elif i + K < num:
            cost += (num - i - K)

    min_ = min(min_, cost)

print(min_)