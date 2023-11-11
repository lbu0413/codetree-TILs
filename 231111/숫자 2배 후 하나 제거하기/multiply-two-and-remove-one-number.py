import sys

min_ = sys.maxsize

N = int(input())
nums = list(map(int, input().split()))

for i in range(N):
    nums[i] *= 2

    for j in range(N):
        sum_ = 0
        tmp = []
        for k in range(N):
            if j != k:
                tmp.append(nums[k])
        
        for k in range(N-2):
            sum_ += abs(tmp[k + 1] - tmp[k])
        min_ = min(min_, sum_)
        
    nums[i] //= 2

print(min_)