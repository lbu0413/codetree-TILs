import sys
N = int(input())

hills = [int(input()) for _ in range(N)]

MAX_H = 100
MIN_ = sys.maxsize
K = 17

for i in range(MAX_H):
    cost = 0
    for j in range(N):
        if hills[j] < i:
            cost += (i - hills[j]) * (i - hills[j])
        
        if hills[j] > i + K:
            cost += ((i + K) - hills[j]) * ((i + K) - hills[j])
    MIN_ = min(MIN_, cost)

print(MIN_)