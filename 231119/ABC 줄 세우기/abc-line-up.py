N = int(input())
people = list(input().split())


cnt = 0

for i in range(1, N):
    j = i - 1
    tmp = people[i]
    while j >= 0 and tmp < people[j]:
        people[j + 1] = people[j]
        j -= 1
        cnt += 1
    people[j + 1] = tmp

print(cnt)