import sys

max_ = -sys.maxsize

N, M = map(int, input().split())
nums = list(map(int, input().split()))


for i in range(N): # 시작 위치 선정
    start = nums[i]
    cnt = 0
    for j in range(M):
        cnt += nums[start-1]
        start = nums[start-1]
    max_ = max(max_, cnt)

print(max_)