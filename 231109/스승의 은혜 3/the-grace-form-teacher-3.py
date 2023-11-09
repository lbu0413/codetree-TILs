import sys

max_ = -sys.maxsize
N, B = map(int, input().split())
presents = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    sorted_p = sorted(presents)
    sorted_p[i][0] //= 2
    cnt = 0
    budget = 0
    for j in range(N):
        if budget + presents[j][0] + presents[j][1] <= B:
            budget += presents[j][0] + presents[j][1]
            cnt += 1

    max_ = max(max_, cnt) 
    

print(max_)