a, b = map(int, input().split())
c, d = map(int, input().split())

nums = [a, b, c, d]

if b <= c or d <= a:
    ans = (b - a) + (d - c)

else:
    if max(nums) == d:
        ans = d - a
    else:
        ans = b - c

print(ans)