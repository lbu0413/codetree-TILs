import sys

N = int(input())
max_ = -sys.maxsize

cups = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, 4): # 조약돌 위치 선정
    pos = i
    scores = 0
    for j in range(N):
        a, b, c = cups[j]
        if pos == a: # a와 b 교환
            pos = b
        elif pos == b:
            pos = a
        if pos == c:
            scores += 1
    max_ = max(max_, scores)

print(max_)