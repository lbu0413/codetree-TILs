N = int(input())





x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]




for i in range(N):
    direction, amnt = map(str, input().split())
    amnt = int(amnt)

    if direction == 'N':
        x += dx[3] * amnt
        y += dy[3] * amnt

    if direction == 'E':
        x += dx[0] * amnt
        y += dy[0] * amnt
    
    if direction == 'S':
        x += dx[1] * amnt
        y += dy[1] * amnt
    
    if direction == 'W':
        x += dx[2] * amnt
        y += dy[2] * amnt


print(x, y)