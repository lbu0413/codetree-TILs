import sys 
max_ = -sys.maxsize
n, m = map(int, input().split())

pairs = [tuple(map(int, input().split())) for _ in range(m)]


for i in range(m):
    cnt = 0
    for a, b in pairs:
        if (pairs[i][0] == a and pairs[i][1] == b) or (pairs[i][0] == b and pairs[i][1] == a):
            cnt += 1
    
    max_ = max(max_, cnt)

print(max_)