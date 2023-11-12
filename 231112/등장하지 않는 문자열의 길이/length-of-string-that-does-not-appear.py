import sys

min_ = sys.maxsize
MAX = 100 + 1

N = int(input())
str_input = input()

cnt = 0

for i in range(N):
    part = str_input[:i+1]
    for j in range(i+1, N-i):
        if str_input[j:j+i+1] == part:
            cnt += 1

print(cnt+1)