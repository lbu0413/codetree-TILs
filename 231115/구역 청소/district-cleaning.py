a, b = map(int, input().split())
c, d = map(int, input().split())

N = max(a, b, c, d)

arr = [0] * (N + 1)
for i in range(a, b+1):
    arr[i] = 1

for j in range(c, d+1):
    arr[j] = 1

cnt = 0
for k in arr:
    if k == 1:
        cnt += 1

print(cnt - 1)