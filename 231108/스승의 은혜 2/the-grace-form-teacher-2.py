import sys

max_ = -sys.maxsize

N, B = map(int, input().split())
presents = [int(input()) for _ in range(N)]

# 반 값으로 할인 받는 선물
for i in range(N):
    cnt = 1
    budget = (presents[i] // 2)
    for j in range(i+1, N): # 나머지 선물
        if budget >= B:
            break
        budget += presents[j]
        cnt += 1
    
    max_ = max(max_, cnt)

print(max_)