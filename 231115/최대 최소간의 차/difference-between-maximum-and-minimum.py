N, K = map(int, input().split())

nums = list(map(int, input().split()))



cost = 0

for i in range(N):
    for j in range(i + 1, N):
        if i == j:
            continue

        if abs(nums[j] - nums[i]) > K and nums[j] - nums[i] < 0:
            nums[j] += 1
            cost += 1
        
        elif abs(nums[j] - nums[i]) > K:
            nums[j] -= 1
            cost += 1

print(cost)