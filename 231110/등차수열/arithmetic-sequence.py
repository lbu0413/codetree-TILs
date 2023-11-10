N = int(input())

nums = list(map(int, input().split()))
max_ = 100 + 1

cnt = 0
for k in range(1, max_):
    for i in range(N):
        for j in range(i+1, N):
            if abs(nums[i] - k) == abs(nums[j] - k):
                cnt += 1



print(cnt)