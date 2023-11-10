import sys

max_ = -sys.maxsize
N, B = map(int, input().split())

n_arr, b_arr = [], []

for i in range(N):
    n, b = map(int, input().split())
    n_arr.append(n)
    b_arr.append(b)


for i in range(N):
    t_arr = [0] * N

    for j in range(N):
        t_arr[j] = n_arr[j] + b_arr[j]
    
    t_arr[i] = n_arr[i] // 2 + b_arr[i]

    t_arr.sort()

    budget, cnt = 0, 0
    
    for k in range(N):
        if budget + t_arr[k] > B:
            break
        budget += t_arr[k]
        cnt += 1
    max_ = max(max_, cnt)

print(max_)