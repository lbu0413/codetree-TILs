a, b = map(int, input().split())
c, d = map(int, input().split())

nums = [a, b, c, d]

if b <= c or d <= a:
    ans = (b - a) + (d - c)

else:
    ans = max(nums) - min(nums)

print(ans)