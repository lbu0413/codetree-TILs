N, M = map(int, input().split())
nums = list(map(int, input().split()))


# 와이파이 한 대가 커버할 수 있는 범위
cover = 2 * M + 1

cnt, i = 0, 0

while True:
    if i >= N:
        break
    
    if nums[i] == 1:
        cnt += 1
        i += 2 * M + 1
    
    else:
        i += 1

print(cnt)