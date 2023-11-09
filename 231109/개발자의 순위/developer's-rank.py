K, N = map(int ,input().split())

ranks = [list(map(int, input().split())) for _ in range(K)]

checker = []
counter = [0] * (N + 1)
for i in range(K):
    for j in range(N):
        for k in range(j+1, N):
            greater_num = ranks[i][j]
            smaller_num = ranks[i][k]
            if i == 0:
                checker.append((greater_num, smaller_num))
                counter[greater_num] += 1
            else:
                if (greater_num, smaller_num) in checker:
                    counter[greater_num] += 1

ans = 0
for i in counter:
   ans += (i // K)

print(counter)
print(ans)