N = int(input())

nums = list(map(int, input().split()))
max_ = max(nums)

cnt = 0
for i in range(N-1):
    for j in range(1, 101):
        for k in range(i+1, N):
            if nums[i] + nums[k] == j * 2:
                cnt += 1

print(cnt)