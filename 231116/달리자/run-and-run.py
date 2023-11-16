import sys


N = int(input())

nums_A = list(map(int, input().split()))
nums_B = list(map(int, input().split()))


cnt = 0
for i in range(N - 1):
    if nums_A[i] > nums_B[i]:
        diff = nums_A[i] - nums_B[i]
        nums_A[i] -= diff
        nums_A[i + 1] += diff
        cnt += diff

print(cnt)