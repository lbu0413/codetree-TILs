import sys

N = 6
min_ = sys.maxsize
max_ = -sys.maxsize

developers = sorted(list(map(int, input().split())))


for i in range(N):
    sum_ = developers[i] + developers[N-i-1]
    max_ = max(max_, sum_)
    min_ = min(min_, sum_)

print(max_ - min_)