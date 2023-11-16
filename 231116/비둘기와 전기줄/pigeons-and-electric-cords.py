N = int(input())

pigeons = [tuple(map(int, input().split())) for _ in range(N)]

cross = [0] * 11

for pigeon, num in pigeons:
    cross[pigeon] += 1

for i in range(len(cross)):
    cross[i] //= 2

print(sum(cross))