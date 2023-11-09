max_ = -1
ans = 0
x, y = map(int, input().split())

for i in range(x, y+1):
    q = i // 10
    r = i % 10

    option = q+r
    
    max_ = max(max_, option)

print(max_)