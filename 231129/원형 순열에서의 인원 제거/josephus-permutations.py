from collections import deque
N, K = map(int, input().split())
nums = deque(list(range(1, N + 1)))


while nums:
    for j in range(K - 1):
        nums.append(nums.popleft())
    print(nums.popleft(), end=" ")