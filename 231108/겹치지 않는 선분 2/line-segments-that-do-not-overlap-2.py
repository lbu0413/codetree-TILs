import sys

N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]

cnt = 0
# 이 첫번째 for문은 처음 기준이 될 선분을 고르는 for문이다. 
for i in range(N):
    overlap = False
    for j in range(N): # 이 두번째 for문은 처음 기준 선분과 돌아가면서 비교가 될 선분이다.
        if i == j:
            continue # 나와 똑같은 선분을, 즉 내 자신과 비교할 필요는 없다
        
        if (lines[i][0] <= lines[j][0] and lines[i][1] >= lines[j][1]) or\
        (lines[i][0] >= lines[j][0] and lines[i][1] <= lines[j][1]):
            overlap = True
            break
    
    else:
        cnt += 1

print(cnt)