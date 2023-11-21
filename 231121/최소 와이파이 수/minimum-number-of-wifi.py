N, M = map(int, input().split())
nums = list(map(int, input().split()))


# 와이파이 한 대가 커버할 수 있는 범위
cover = 2 * M + 1

print(N // cover)