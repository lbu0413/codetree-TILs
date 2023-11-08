import sys

max_ = -sys.maxsize

N, B = map(int, input().split())
presents = [int(input()) for _ in range(N)]

# 반 값으로 할인 받는 선물
for i in range(N):
    cnt = 0
    for j in range(N): # 나머지 선물
        if j == i:
            B -= (presents[j] // 2)
            cnt += 1
            continue
        
        B -= presents[j]
        cnt += 1

        if B <= 0:
            break
    max_ = max(max_, cnt)
print(max_)