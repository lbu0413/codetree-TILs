import sys

N = int(input())
MAX = 1000 + 1

adjacent_sums = list(map(int, input().split()))
arr = [0] * N

for i in range(1, N + 1):
    arr[0] = i
    for j in range(1, N):
        arr[j] = adjacent_sums[j - 1] - arr[j - 1]
    
    # 배열에는 1이상 N이하의 숫자들이 단 한번씩만 등장해야함.
    satisfied = True
    exists = [False] * (N + 1)

    for j in range(N):
        if arr[j] < 1 or arr[j] > N:
            satisfied = False
        
        if exists[arr[j]]:
            satisfied = False
        exists[arr[j]] = True
    
    if satisfied:
        for x in arr:
            print(x, end=" ")
        sys.exit(0)