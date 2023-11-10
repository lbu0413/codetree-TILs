N = int(input())

nums = list(map(int, input().split()))
max_ = 100 + 1

ans = 0
for k in range(1, max_):
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if nums[i] + nums[j] == k * 2:
                cnt += 1

    ans = max(ans, cnt)


print(cnt)