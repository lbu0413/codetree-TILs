import sys

max_ = -sys.maxsize
N, B = map(int, input().split())
presents = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    tmp = [presents[k] for k in range(N)]
    tmp[i][0] //= 2
    cnt = 0
    budget = 0
    for j in range(N):
        if budget + tmp[j][0] + tmp[j][1] <= B:
            budget += tmp[j][0] + tmp[j][1]
            cnt += 1

    max_ = max(max_, cnt) 
    

print(max_)