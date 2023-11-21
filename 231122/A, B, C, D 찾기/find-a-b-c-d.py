nums = list(map(int, input().split()))
n = len(nums)
nums.sort()

a = nums[0]
b = nums[1]
c = nums[2]

abcd = nums[n-1]
abc = a + b + c
d = abcd - abc
print(a, b, c, d)