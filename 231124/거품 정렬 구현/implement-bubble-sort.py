N = int(input())

nums = list(map(int, input().split()))


for i in range(N):
    for j in range(N - 1):
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp

print(*nums)