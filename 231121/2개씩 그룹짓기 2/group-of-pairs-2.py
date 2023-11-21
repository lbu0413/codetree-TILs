import sys

min_ = sys.maxsize

N = int(input())

nums = sorted(list(map(int, input().split())))


for i in range(N):
    option = nums[N+i] - nums[i]

    min_ = min(min_, option)

print(min_)