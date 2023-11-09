K, N = map(int, input().split())

ranks = [list(map(int, input().split())) for _ in range(K)]

pairs_count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        valid_pair = True
        for k in range(K):
            if ranks[k].index(i) > ranks[k].index(j):
                valid_pair = False
                break
        if valid_pair and i != j:
            pairs_count += 1

print(pairs_count)