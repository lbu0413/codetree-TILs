N = int(input())

people = list(input().split())
cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        if people[i] > people[j]:
            people[i], people[j] = people[j], people[i]
            cnt += 1
            break

print(cnt)