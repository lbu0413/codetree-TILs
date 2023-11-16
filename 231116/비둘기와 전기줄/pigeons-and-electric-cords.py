N = int(input())

pigeons = [tuple(map(int, input().split())) for _ in range(N)]

check1 = ["X"] * 11
check2 = [0] * 11

for i in range(N):
    pigeon, num = pigeons[i]
    if (check1[pigeon] == 0 and num == 1) or (check1[pigeon] == 1 and num == 0):
        check2[pigeon] += 1
    
    else:
        check1[pigeon] = num

print(sum(check2))