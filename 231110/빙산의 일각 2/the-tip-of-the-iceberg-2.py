import sys
max_ = -sys.maxsize

N = int(input())
icebergs = [int(input()) for _ in range(N)]
limit = 1000 + 1

for i in range(1, limit):
    cnt = 0
    previous = False
    for j in icebergs:
        if j > i:
            if previous:
                cnt += 1
            else:
                previous = False
                cnt = 1
        
        elif j <= i:
            previous = True

    max_ = max(max_, cnt)

print(max_)