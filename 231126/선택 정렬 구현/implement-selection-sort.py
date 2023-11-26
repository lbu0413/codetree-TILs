# 1. 전체 값 중 가장 작은 값을 찾음
# 2. 해당 값을 맨 첫번째에 배치함
# 3. 첫번째 값을 제외하고 가장 작은 값을 찾아 두번째에 배치함
# 4. 두번째, 세번째, ... n-1번째 값을 제외하고 가장 작은 값을 찾아 정해진 위치에 배치함.

N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    min_idx = i
    for j in range(i + 1, N):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]


print(*arr)