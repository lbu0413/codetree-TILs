import sys

N = int(input())
lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

MAX = 100 + 1

arr = [0] * MAX

for x, y in lines:
    for i in range(x, y+1):
        arr[i] += 1

for x, y in lines:
    for j in range(x, y+1):
        arr[j] -= 1
    
    for k in range(MAX):
        if arr[k] > 1:
            print("Yes")
            sys.exit()

print("No")