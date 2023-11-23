N = int(input())
nums = list(map(int, input().split()))


for i in range(N):
    min_ = i
    for j in range(i + 1, N):
        if nums[j] < nums[min_]:
            min_ = j
    
    tmp = nums[i]
    nums[i] = nums[min_]
    nums[min_] = tmp

print(*nums)