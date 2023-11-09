import sys

N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            overlap = False
            arr = [0] * (100 + 1)

            for m in range(N):
                if m == i or m == j or m == k:
                    continue
                for x in range(lines[m][0], lines[m][1]+1):
                    arr[x] += 1
                
            
            for y in range(101):
                if arr[y] > 1:
                    overlap = True
            
            if not overlap:
                ans += 1

print(ans)