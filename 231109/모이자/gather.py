import sys

N = int(input())
distance = list(map(int, input().split()))
min_ = sys.maxsize

for i in range(N):
    sum_, move_ = 0, 0
    for j in range(N):
        destination = distance[i]
        if j == i:
            move_ = 0
        else:
            move_ = abs(j-i)
        
        sum_ += (distance[j] * move_)
    min_ = min(min_, sum_)

print(min_)