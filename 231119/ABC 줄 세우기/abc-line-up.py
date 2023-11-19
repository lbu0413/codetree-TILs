import sys
N = int(input())

min_ = sys.maxsize

people = list(input().split())

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if people[i] > people[j]:
            people[i], people[j] = people[j], people[i]
            cnt += 1
        break


cnt2 = 0
for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1 -1):
        if people[i] < people[j]:
            people[i], people[j] = people[j], people[i]
            cnt2 += 1
        break

if cnt == 0:
    print(cnt2)

elif cnt2 == 0:
    print(cnt)

else:
    print(min(cnt, cnt2))