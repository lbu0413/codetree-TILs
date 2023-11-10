import sys

T, a, b = map(int, input().split())

arr = [tuple(map(str, input().split())) for _ in range(T)]


cnt = 0 
for i in range(a, b+1):
    s_num, n_num = sys.maxsize, sys.maxsize
    for alpha, pos in arr:
        pos = int(pos)
        if alpha == 'S':
            s_num = min(s_num, abs(i - pos))
        else:
            n_num = min(n_num, abs(i - pos))
    
    if s_num <= n_num:
        cnt += 1

print(cnt)