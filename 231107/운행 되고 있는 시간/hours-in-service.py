import sys
max_ = -sys.maxsize
N = int(input())

MAX = 1000 + 1
time = [tuple(map(int, input().split())) for _ in range(N)]



# 해고 할 직원을 구한다
for i in range(N):
    cnt = [0] * MAX
    for j, (start, end) in enumerate(time):
        if j == i:
            continue
        
        # 나머지 직원들의 스케쥴을 카운트 배열에 집어넣는다.
        for k in range(start, end):
            cnt[k] += 1
            
    working_hours = 0    
    for j in range(1, MAX):
        if cnt[j] > 0:
            working_hours += 1
    
    max_ = max(max_, working_hours)


print(max_)