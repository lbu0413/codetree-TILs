import sys

min_ = sys.maxsize


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

MAX = 101

for i in range(1, MAX):
    for j in range(1, MAX):
        max_ = 0
        ul, ur, dl, dr = 0, 0, 0, 0
        for x, y in points:
            # if x == i or y == j:
            #     continue
            # up-left
            if x <= i and y >= j:
                ul += 1
            
            # up-right
            if x >= i and y >= j:
                ur += 1
            
            # down-left
            if x <= i and y <= j:
                dl += 1
            
            # down-right
            if x >= i and y <= j:
                dr += 1

            max_ = max(ul, ur, dl, dr)
        
        min_ = min(min_, max_)

print(min_)