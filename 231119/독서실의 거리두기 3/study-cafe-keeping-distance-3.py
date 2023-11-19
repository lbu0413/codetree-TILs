import sys



N = int(input())
seats = list(input())


max_dist = 0
max_i = -1
max_j = -1
for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                if j - i > max_dist:
                    max_i = i
                    max_j = j
                    break

seats[(max_j - max_i) // 2 + max_i] = '1'

ans = sys.maxsize
for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                ans = min(ans, j - i)

print(ans)