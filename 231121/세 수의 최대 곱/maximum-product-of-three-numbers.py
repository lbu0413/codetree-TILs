N = int(input())

nums = sorted(list(map(int, input().split())))


option1 = nums[0] * nums[1] * nums[-1]
option2 = nums[-1] * nums[-2] * nums[-3]

print(max(option1, option2))