import sys
N = int(input())

min_ = sys.maxsize

people = list(input().split())

for k in range(N):
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if people[i] > people[j]:
                people[i], people[j] = people[j], people[i]
                cnt += 1
            break
    min_ = min(min_, cnt)

print(min_)