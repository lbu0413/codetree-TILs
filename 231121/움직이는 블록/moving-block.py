N = int(input())

nums = [int(input()) for i in range(N)]

avg = sum(nums) // N

cnt = 0

for i in nums:
    if i > avg:
        cnt += (i - avg)

print(cnt)