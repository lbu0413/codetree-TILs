a, b = map(int, input().split())
c, d = map(int, input().split())

if c <= b:
    ans = d - a

elif a <= d:
    ans = b - c

else:
    ans = (b - a) + (d - c)

print(ans)