import sys
N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

min_line = sys.maxsize
for i in range(N):
    min_point = sys.maxsize
    max_point = -sys.maxsize
    for j in range(N):
        if i == j:
            continue

        start, end = lines[j]

        if start < min_point:
            min_point = start
        
        if end > max_point:
            max_point = end
    
    min_line = min(min_line, max_point - min_point)


print(min_line)