N = int(input())

pigeons = [tuple(map(int, input().split())) for _ in range(N)]

check = [-1] * 11

cnt = 0
for i in range(N):
    pigeon, num = pigeons[i]
    if check[pigeon] == -1:
        check[pigeon] = num
    
    elif check[pigeon] != num:
        check[pigeon] = num
        cnt += 1


print(cnt)