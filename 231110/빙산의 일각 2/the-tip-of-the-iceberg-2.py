import sys
max_ = -sys.maxsize

N = int(input())
icebergs = [int(input()) for _ in range(N)]
limit = 1000 + 1

for i in range(1, limit):
    cnt = 0
    prev = True 
    for j in icebergs:
        if i < j:
            if prev:
                cnt += 1
                prev = False
            else:
                cnt = 1
        else:
            prev = True

    max_ = max(max_, cnt)

print(max_)