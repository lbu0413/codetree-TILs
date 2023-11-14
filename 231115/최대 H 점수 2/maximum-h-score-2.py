N, L = map(int, input().split())
nums = list(map(int, input().split()))


ans = 0
for i in range(1, N + 1):
    cnt = 0
    cntL = 0

    for j in range(N):
        if nums[j] >= i:
            cnt += 1
        
        elif nums[j] == i - 1:
            if cntL < L:
                cntL += 1
                cnt += 1
    
    if cnt >= i:
        ans = i

print(ans)