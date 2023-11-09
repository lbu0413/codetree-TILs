max_ = -1
ans = 0
x, y = map(int, input().split())

for i in range(x, y+1):
    sum_ = 0
    while i:
        sum_ += i % 10
        i = i // 10
    ans = sum_
    max_ = max(max_, ans)

print(max_)