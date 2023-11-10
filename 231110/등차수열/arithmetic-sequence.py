N = int(input())

nums = list(map(int, input().split()))
max_ = max(nums)

cnt = 0
for i in range(N):
    for j in range(i+1, max_):
        for k in range(i+1, N):
            if abs(nums[i] - j) == abs(nums[k] - j) and k > i:
                cnt += 1

print(cnt)