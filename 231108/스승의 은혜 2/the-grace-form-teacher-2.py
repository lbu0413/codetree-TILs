import sys

max_ = -sys.maxsize

N, B = map(int, input().split())
presents = [int(input()) for _ in range(N)]

# 반 값으로 할인 받는 선물
for i in range(N):
    cnt = 0
    budget = 0
    for j in range(N): # 나머지 선물
        if j == i:
            budget += (presents[j] // 2)
            cnt += 1
            continue
          
        budget += presents[j]

        if budget >= B:
            break 
        
        cnt += 1

    max_ = max(max_, cnt)

print(max_)