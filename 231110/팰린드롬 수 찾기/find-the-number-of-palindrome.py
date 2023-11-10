x, y = map(int, input().split())

cnt = 0

for i in range(x, y+1):
    num = str(i)
    n = len(num)
    for j in range(n//2):
        if num[j] != num[n-j-1]:
            break
    else:
        cnt += 1

print(cnt)