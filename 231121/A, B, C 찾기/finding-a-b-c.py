nums = sorted(list(map(int, input().split())))

A = min(nums)

ABC = max(nums)

if ABC - A in nums:
    BC = ABC - A

B = nums[1]
C = BC - B

print(A, B, C)