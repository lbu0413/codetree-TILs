K, N = map(int, input().split())

ranks = [list(map(int, input().split())) for _ in range(K)]

pairs_count = 0

for i in range(N):
    for j in range(N):
        valid_pair = True
        for k in range(K):
            if ranks[k].index(i+1) > ranks[k].index(j+1):
                valid_pair = False
                break
        if valid_pair and i != j:
            pairs_count += 1

print(pairs_count)