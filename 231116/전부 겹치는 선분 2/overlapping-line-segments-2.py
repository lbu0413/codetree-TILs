import sys

N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j and i == k:
                continue
            
            if lines[j][1] < lines[k][0] or lines[k][1] < lines[j][0]:
                ans = " No"
            
            else:
                print("Yes")
                sys.exit()

print(ans)