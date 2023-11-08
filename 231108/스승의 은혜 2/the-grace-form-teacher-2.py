import sys

max_ = -sys.maxsize

N, B = map(int, input().split())
presents = [int(input()) for _ in range(N)]


for i in range(N):
    tmp = [presents[j] for j in range(N)]
    tmp[i] //= 2
    
    tmp.sort()
    cnt = 0
    budget = 0


    for j in range(N):
        if budget + tmp[j] > B:
            break
        budget += tmp[j]
        cnt += 1
    
    max_ = max(max_, cnt)


print(max_)